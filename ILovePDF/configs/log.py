# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/configs/log.py"

import os
import logging
from datetime import datetime

class log:
    
    # Logging Configuration
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", False)
    LOG_FILE = os.environ.get("LOG_FILE", None)  # Set to None by default
    
    # Log Level Configuration
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
    
    @staticmethod
    def setup_logging():
        """Setup logging configuration"""
        log_format = "[%(asctime)s - %(name)s] : %(levelname)s - %(message)s"
        
        # Create logs directory if it doesn't exist
        os.makedirs("logs", exist_ok=True)
        
        # Set log file path
        if not log.LOG_FILE:
            log.LOG_FILE = "logs/iLovePDF.log"
        
        # Configure logging
        logging.basicConfig(
            level=getattr(logging, log.LOG_LEVEL, logging.INFO),
            format=log_format,
            handlers=[
                logging.FileHandler(log.LOG_FILE),
                logging.StreamHandler()
            ]
        )
    
    @staticmethod
    async def footer(message, output=None, lang_code="eng", coffee=False):
        """Log footer information"""
        try:
            # Log the completion
            if output:
                log_msg = f"Task completed for user {message.from_user.id}"
                if hasattr(output, 'file_name'):
                    log_msg += f" - File: {output.file_name}"
                logging.info(log_msg)
            
            # Send simple completion message
            await message.reply_text("✅ Task completed successfully!", quote=True)
                
        except Exception as e:
            logging.error(f"Error in footer logging: {e}")

# Initialize logging when module is imported
log.setup_logging()

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
