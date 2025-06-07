# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/plugins/dm/callBack/__index__.py"

from pdf import PDF
from plugins import *
from plugins.utils import *
from configs.db import CUSTOM_THUMBNAIL_U, CUSTOM_THUMBNAIL_C, myID

@ILovePDF.on_callback_query(filters.regex("^index"))
async def __index__(bot, callbackQuery):
    try:
        lang_code = await util.getLang(callbackQuery.message.chat.id)
        
        if await render.header(bot, callbackQuery, lang_code, doc=False):
            return

        await callbackQuery.answer()
        data = callbackQuery.data
        userId, chatId = callbackQuery.from_user.id, callbackQuery.message.chat.id

        _, __ = data.split("|", 1)

        try:
            if __ == "pages":
                # Show page selection
                await callbackQuery.edit_message_text(
                    text="Please select pages...",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("All Pages", callback_data="index|all"),
                        InlineKeyboardButton("Custom", callback_data="index|custom")
                    ]])
                )
            
            elif __ == "all":
                # Process all pages
                await callbackQuery.answer("Processing all pages...")
                # Add your processing logic here
                
            elif __ == "custom":
                # Ask for custom page range
                await callbackQuery.edit_message_text(
                    text="Please enter page numbers (e.g., 1,3,5 or 1-5):",
                )
                # Add your custom page logic here
                
            else:
                # Get translation for INDEX
                try:
                    CHUNK, btn = await util.translate(
                        text="INDEX", 
                        button="INDEX['button']" if "button" in ["INDEX"] else None,
                        lang_code=lang_code
                    )
                    
                    # Handle if CHUNK is a string instead of dict
                    if isinstance(CHUNK, str):
                        process_text = "Processing your request..."
                    elif isinstance(CHUNK, dict) and "process" in CHUNK:
                        process_text = CHUNK["process"]
                    else:
                        process_text = "Processing your request..."
                        
                    await callbackQuery.answer(process_text)
                    
                except Exception as e:
                    logger.debug(f"Translation error in index: {e}")
                    await callbackQuery.answer("Processing...")

        except Exception as e:
            logger.debug(f"Error in index callback: {e}")
            await callbackQuery.answer("An error occurred")
            
    except Exception as e:
        logger.exception("🐞 %s: %s" % (file_name, e), exc_info=True)

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
