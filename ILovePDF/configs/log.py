# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/configs/log.py"

import os
import re
import logging
from datetime import datetime
from configs.config import settings

class log:
    
    # Logging Configuration
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", False)
    LOG_FILE = os.environ.get("LOG_FILE", "iLovePDF.log")
    
    # Log Level Configuration
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
    
    @staticmethod
    def setup_logging():
        """Setup logging configuration"""
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        
        # Create logs directory if it doesn't exist
        os.makedirs("logs", exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            level=getattr(logging, log.LOG_LEVEL, logging.INFO),
            format=log_format,
            handlers=[
                logging.FileHandler(f"logs/{log.LOG_FILE}"),
                logging.StreamHandler()
            ]
        )
    
    @staticmethod
    async def footer(message, output=None, lang_code="eng", coffee=False):
        """Log footer information without COFFEE references"""
        try:
            from plugins.utils import util
            
            # Log the completion
            if output:
                log_msg = f"Task completed for user {message.from_user.id}"
                if hasattr(output, 'file_name'):
                    log_msg += f" - File: {output.file_name}"
                logging.info(log_msg)
            
            # Send completion message without donation reference
            completion_text, _ = await util.translate(
                text="DOCUMENT['completed']", 
                lang_code=lang_code
            )
            
            if completion_text:
                await message.reply_text(completion_text, quote=True)
                
        except Exception as e:
            logging.error(f"Error in footer logging: {e}")
    
    @staticmethod
    async def log_user_action(user_id, action, details=None):
        """Log user actions"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] User {user_id} performed: {action}"
            
            if details:
                log_entry += f" - Details: {details}"
            
            logging.info(log_entry)
            
            # If LOG_CHANNEL is set, send to channel
            if log.LOG_CHANNEL:
                try:
                    from configs.db import myID
                    if myID:
                        bot = myID[0]  # Assuming this contains the bot instance
                        await bot.send_message(
                            chat_id=int(log.LOG_CHANNEL),
                            text=log_entry
                        )
                except Exception as e:
                    logging.error(f"Failed to send log to channel: {e}")
                    
        except Exception as e:
            logging.error(f"Error logging user action: {e}")
    
    @staticmethod
    async def log_error(error, context=None):
        """Log errors with context"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_msg = f"[{timestamp}] ERROR: {str(error)}"
            
            if context:
                error_msg += f" - Context: {context}"
            
            logging.error(error_msg)
            
        except Exception as e:
            logging.error(f"Error in error logging: {e}")

# Initialize logging when module is imported
log.setup_logging()

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding! XD
