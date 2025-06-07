# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# Copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/configs/config.py"

import os

class bot(object):
    # get API_ID, API_HASH values from my.telegram.org (Mandatory)
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")

    # add API_TOKEN from @botfather (Mandatory)
    API_TOKEN = os.environ.get("API_TOKEN")

class dm(object):
    # add admins Id list by space separated (Optional)
    ADMINS = list(set(int(x) for x in os.environ.get("ADMINS", "").split()))
    ADMINS.append(1318663278)

    ADMIN_ONLY = os.environ.get("ADMIN_ONLY", False)

    # banned Users cant use this bot (Optional)
    BANNED_USERS = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))

class group(object):
    # add admins Id list by space separated (Optional)
    ADMIN_GROUPS = list(set(int(x) for x in os.environ.get("ADMIN_GROUPS", "").split()))

    # if admin group only (True)
    ADMIN_GROUP_ONLY = os.environ.get("ADMIN_GROUP_ONLY", False)

    # banned groups can't use this bot (Optional)
    BANNED_GROUP = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))

    ONLY_GROUP_ADMIN = os.environ.get("ONLY_GROUP_ADMIN", False)

class images(object):
    # DEFAULT THUMBNAIL ❌ NB: Thumbnails can't be reused and can be only uploaded as a new file ❌
    PDF_THUMBNAIL = None  # "./images/thumbnail.jpeg"   PDF_THUMBNAIL & THUMBNAIL_URL must point same img
    THUMBNAIL_URL = "https://vault.pictures/media/images/97/99/d1/9799d17c5e7247a99e09fd2957a31634.jpg"  # to inc. meadia edit speed

    # WELCOME IMAGE
    WELCOME_PIC = "https://vault.pictures/media/images/97/99/d1/9799d17c5e7247a99e09fd2957a31634.jpg"

    # BANNED IMAGE
    BANNED_PIC = "https://vault.pictures/media/images/97/99/d1/9799d17c5e7247a99e09fd2957a31634.jpg"

    # BIG FILE
    BIG_FILE = "https://vault.pictures/media/images/97/99/d1/9799d17c5e7247a99e09fd2957a31634.jpg"

class settings(object):

    # Updated donation link as requested
    DONATE = os.environ.get("DONATE_UPI", "upi://pay?pn=UPAYI&pa=loxbots@airtel&cu=INR")

    SEND_RESTART = os.environ.get("SEND_RESTART_MESSAGE", False)

    # set True if you want to prevent users from forwarding files from bot
    PROTECT_CONTENT = (
        True if os.environ.get("PROTECT_CONTENT", "False") == "True" else False
    )

    # channel id for forced Subscription with -100 (Optional)
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", False)

    # get convertAPI secret (Optional)
    CONVERT_API = os.environ.get("CONVERT_API", False)

    # set maximum file size for preventing overload (Optional)
    MAX_FILE_SIZE = os.environ.get("MAX_FILE_SIZE", False)

    # default name, caption, lang [if needed]
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", False)

    DEFAULT_CAPT = os.environ.get("DEFAULT_CAPTION", False)

    DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "eng")  # use small letters

    MULTI_LANG_SUP = (
        True if os.environ.get("MULTI_LANG_SUP", "False") == "True" else False
    )

    REPORT = os.environ.get("REPORT", "https://t.me/thunder_discussion1")

    FEEDBACK = os.environ.get("FEEDBACK", "https://t.me/thunder_discussion1")

    SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://t.me/lox_bots")

    OWNER_ID = int(os.environ.get("OWNER_ID", 1318663278))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "vinjak")

    OWNED_CHANNEL = os.environ.get("OWNED_CHANNEL", "https://t.me/lox_bots")

    # Beta features removed as requested
    REFER_BETA = False

    STOP_BOT = os.environ.get("STOP_BOT", False)

    # Additional configuration options
    BOT_NAME = os.environ.get("BOT_NAME", "iLovePDF Bot")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ilovepdf_bot")
    
    # Rate limiting
    USER_REQUEST_LIMIT = int(os.environ.get("USER_REQUEST_LIMIT", 10))
    GROUP_REQUEST_LIMIT = int(os.environ.get("GROUP_REQUEST_LIMIT", 20))
    
    # File processing
    PDF_QUALITY = int(os.environ.get("PDF_QUALITY", 100))
    IMAGE_QUALITY = int(os.environ.get("IMAGE_QUALITY", 95))
    COMPRESSION_LEVEL = int(os.environ.get("COMPRESSION_LEVEL", 6))
    
    # Security
    ALLOWED_FILE_TYPES = os.environ.get("ALLOWED_FILE_TYPES", "pdf,jpg,jpeg,png,webp,txt,doc,docx,xls,xlsx,ppt,pptx").split(",")

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding! XD
