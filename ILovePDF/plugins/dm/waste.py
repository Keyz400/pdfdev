# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/plugins/dm/waste.py"

from plugins import *
from plugins.utils import *
from configs.config import dm


# WASTE/SPAMMING MESSAGES 
@ILovePDF.on_message(filters.private & filters.incoming & ~filters.user(dm.ADMINS) & ~filters.sticker)
async def _spam(bot, message):
    try:
        lang_code = await util.getLang(message.chat.id)
        await message.reply_chat_action(enums.ChatAction.TYPING)
        tTXT, tBTN = await util.translate(text="noHelp", lang_code=lang_code)
        await message.reply_text(tTXT, quote=True)
    except Exception as e:
        logger.exception("🐞 %s: %s" % (file_name, e), exc_info=True)


# HANDLE STICKERS - Removed specific sticker ID and disabled sticker responses
@ILovePDF.on_message(filters.private & filters.sticker & filters.incoming)
async def handle_stickers(bot, message):
    try:
        # Sticker handling disabled as requested
        # The specific sticker ID "CAACAgIAAxkBAAEOjNtoMJIwYLbXxQYOWU0EcDgKON4TkAACVQADr8ZRGmTn_PAl6RC_NgQ" has been removed
        lang_code = await util.getLang(message.chat.id)
        tTXT, tBTN = await util.translate(text="noHelp", lang_code=lang_code)
        await message.reply_text(tTXT, quote=True)
    except Exception as e:
        logger.exception("🐞 %s: %s" % (file_name, e), exc_info=True)

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
