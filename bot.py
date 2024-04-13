from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "JABWA",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    await bot.send_message("L_HLN", "**تم تشغيل الصانع عزيزي زين. **")
    print("تم تشغيل الصانع بنجاح")
    await idle()
