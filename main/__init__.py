#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24715454
API_HASH = "6300b296b551b142987266d1d1a00690"
BOT_TOKEN = "6180921346:AAEGokqsOm86Ikzk8KXTw-buuL6dhhYqkVU"
SESSION = "BQClD67YT8hFBCwa5i-oNFFrGlbV25TyOQvZuQxzFWQXPnUOo630KQ0h2YMCZqNTKFz_UzOMGOvs0w_W1rCmRYDmiaihT2N_kezvgkUChctl-0VZDBZUxNFHkpLtdjgBB84mOx4FG4PCwv7j4SxM4ypyChUxZkC_i2vp7N7cZvfgfN1SA7nwlrag3_3jOzhry33jou5ObygjVxaP29Fk_LaoiFWTE9SVATVHpjbBRGBLRDIxch_a1c2sTKjdYuKHRDIA5_t_XAjvYzrCOSXOyfYZg7_AfUW069AysKHypWJvPkW93R3jETl4G_7P4aOb-E5u80kqaio9LI1rMPivZy11AAAAAUzh8D4A"
FORCESUB ="loggingtest213"
AUTH =5584842814

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
