# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/plugins/dm/commands.py"

from pdf import PDF
from plugins import *
from plugins.utils import *
from configs.db import myID
from configs.db import dataBASE
from configs.config import dm, settings

if dataBASE.MONGODB_URI:
    from database import db


# ❌ CANCELS CURRENT PDF TO IMAGES WORK ❌
@ILovePDF.on_message((filters.private | filters.group) & filters.command(["cancel"]) & filters.incoming)
async def cancelP2I(bot, message):
    try:
        await work.work(message, "delete", True)
        return await message.delete()
    except Exception:
        pass


# ❌ DELETS CURRENT IMAGES TO PDF QUEUE (/delete) ❌
@ILovePDF.on_message((filters.private | filters.group) & filters.command(["delete"]) & filters.incoming)
async def _cancelI2P(bot, message):
    try:
        lang_code = await util.getLang(message.chat.id)
        await message.reply_chat_action(enums.ChatAction.TYPING)
        del PDF[message.chat.id]
        trans_txt, trans_btn = await util.translate(
            text="GENERATE['deleteQueue']", lang_code=lang_code
        )
        await message.reply_text(trans_txt, quote=True)
        shutil.rmtree(f"work/{message.chat.id}")
    except Exception:
        trans_txt, trans_btn = await util.translate(
            text="GENERATE['noQueue']", lang_code=lang_code
        )
        await message.reply_text(trans_txt, quote=True)


# Beta functionality removed as requested
# The beta command and all related functionality has been disabled

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
