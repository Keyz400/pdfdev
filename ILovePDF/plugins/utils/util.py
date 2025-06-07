# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/plugins/utils/util.py"

import re
import os
import sys
import asyncio
from logger import logger
from configs.config import settings
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Import language modules
try:
    if settings.DEFAULT_LANG:
        exec(f"from lang import {settings.DEFAULT_LANG}")
        logger.debug(f"Successfully imported language: {settings.DEFAULT_LANG}")
    else:
        from lang import eng
        logger.debug("Using default English language")
except Exception as e:
    logger.debug(f"Error importing language {settings.DEFAULT_LANG}: {e}")
    try:
        from lang import eng
        settings.DEFAULT_LANG = "eng"
        logger.debug("Fallback to English language")
    except Exception as e2:
        logger.debug(f"Critical error: Cannot import any language module: {e2}")
        sys.exit(1)

# Language utilities
async def getLang(chat_id):
    """Get language code for chat"""
    try:
        from lang.__users__ import userLang
        return userLang.get(chat_id, settings.DEFAULT_LANG)
    except Exception:
        return settings.DEFAULT_LANG

async def translate(text, lang_code="eng", button=None, order=None):
    """Translate text and buttons to specified language"""
    try:
        # Get the language module
        if lang_code == "eng":
            lang_module = eng
        else:
            try:
                lang_module = __import__(f"lang.{lang_code}", fromlist=[lang_code])
            except ImportError:
                lang_module = eng
                lang_code = "eng"
        
        # Get translated text
        try:
            rtn_text = eval(f"lang_module.{text}")
        except AttributeError:
            # Fallback to English if translation not found
            rtn_text = eval(f"eng.{text}")
        
        # Handle buttons if provided
        rtn_button = None
        if button:
            try:
                rtn_button = eval(f"lang_module.{button}")
                if order:
                    rtn_button = await createBUTTON(btn=rtn_button, order=order)
            except AttributeError:
                try:
                    rtn_button = eval(f"eng.{button}")
                    if order:
                        rtn_button = await createBUTTON(btn=rtn_button, order=order)
                except Exception:
                    rtn_button = None
        
        return rtn_text, rtn_button
        
    except Exception as e:
        logger.exception(f"Translation error for {text}: {e}")
        return f"Translation Error: {text}", None

async def createBUTTON(btn, order=None):
    """Create inline keyboard from button dictionary"""
    try:
        if not btn or not isinstance(btn, dict):
            return None
            
        buttons = []
        if order:
            # Handle ordered button layout
            order_str = str(order)
            current_row = []
            btn_items = list(btn.items())
            btn_index = 0
            
            for char in order_str:
                row_size = int(char)
                row = []
                for _ in range(row_size):
                    if btn_index < len(btn_items):
                        text, callback_data = btn_items[btn_index]
                        if callback_data.startswith("http"):
                            row.append(InlineKeyboardButton(text, url=callback_data))
                        else:
                            row.append(InlineKeyboardButton(text, callback_data=callback_data))
                        btn_index += 1
                if row:
                    buttons.append(row)
        else:
            # Default single column layout
            for text, callback_data in btn.items():
                if callback_data.startswith("http"):
                    buttons.append([InlineKeyboardButton(text, url=callback_data)])
                else:
                    buttons.append([InlineKeyboardButton(text, callback_data=callback_data)])
        
        return InlineKeyboardMarkup(buttons) if buttons else None
        
    except Exception as e:
        logger.exception(f"Button creation error: {e}")
        return None

# Additional utility functions
def format_bytes(size):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f}{unit}"
        size /= 1024.0
    return f"{size:.1f}PB"

async def progress_callback(current, total, message, action="Processing"):
    """Progress callback for file operations"""
    try:
        percentage = current * 100 / total
        progress_str = f"{action}: {percentage:.1f}%"
        
        if percentage % 5 == 0:  # Update every 5%
            try:
                await message.edit_text(progress_str)
            except Exception:
                pass  # Ignore edit errors
    except Exception:
        pass

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
