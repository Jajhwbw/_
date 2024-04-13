import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

OWNER = ["L_HLN","TR_E2S_ON_MY_MOoN"]
OWNER_NAME = "𝐎ꪶ𝐋ٓ𝐄𝐕ِ𝐑"
BOT_TOKEN = getenv("BOT_TOKEN")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
DATABASE = getenv("MONGO_DB_URI", None)
CHANNEL = "https://t.me/sourceav"
GROUP = "https://t.me/va_source"
VID_SO = "https://telegra.ph/file/4fda78aaf200bf313be62.jpg"
PHOTO = "https://telegra.ph/file/4fda78aaf200bf313be62.jpg"
LOGS = "jabababbab"
