import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class autocaption(Client):
            api_id = "3845818",
            api_hash = Config.API_HASH,
            bot_token = Config.BOT_TOKEN,
            workers = 20,
            plugins = dict(
                root="Plugins"
            )
autocaption = Client(
    "captioner",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

if __name__ == "__main__" :
    autocaption().run()

