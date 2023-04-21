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
BOT_TOKEN = "5899286322:AAHkKRbxldFAw093XyrWR7dTdyB47Bugeq0"
SESSION = "BQGpIroAtto--Vtj6cErkAq8rPQcuebEzHA3No6rYMWaSO03GJCBGveKyow1l0_GrxkEtGMyYeGDVROTW5K3VML_D-xf_reU-3x2fLg91hViW0kfx0dzR8Pxi1-FUfEQDVd6u_l7aLlvBzcZRjleMO7gLotgHCzUYE7YzQV7v8rAQhKRfa6VkxOgWn-WYtnkp08VwO2F3hx26dkRLAUW3zGpKH1pxOpiR2RT0zJWQpSgyiCiwyHI94bliC-NgToPxXj4YL2q_PmBegHvlG85ebqQ9FYgEhFEHM1WZZOl-sYV2BxDY441H6bXEmmplzUV_nPHQNhCVcA8XYTx8-vL2xt-2644EQAAAAFPtuRiAA"
FORCESUB = "loggingtest213"
AUTH = 5584842814

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
