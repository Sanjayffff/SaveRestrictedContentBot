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
SESSION = "BQBw7Qu2BMmOcr0O3OvvpJOuto5Re4XVNiF5P9xP_jEOYExpHONk8ubNin91-OM6hSNSU2v5a_vApridN4YE1w7GmbIZ45pr9n6o4SFBZRjhNME-bytk9Yjs78zHDJ714GKq_pxctijBTvlTSJMHSwa0qjhsmbr4CYJFLQOvPs63yfwFP_ORmK9PHqK0-B3IrqIEVCLltnRD9YzJtnos4K2ffdqAHlb97IDIzZtyuoxAg33WD5WDsVmSTWWyE1b4fqBPloo3Ws-AnwFxUm5iK_XnXW-mmXSzHNGpOedre6tVpynXp0AMLxfsAVywuHeriDI6uxYcw7PbH8CBr5E_Bx_wAAAAAU-25GIA"
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
