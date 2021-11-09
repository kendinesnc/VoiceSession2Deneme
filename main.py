from pyrogram import Client as Bot

from pyrogram import idle
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN
from callsmusic import run1
from callsmusic import run2


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()
run1()
run2()
idle() 
