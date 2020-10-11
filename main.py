import logging
from pyrogram import Client
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.getLogger(__name__)

BOT = Client(
    "CheckRestrictionsBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(
        root="plugins"
    )
)

BOT.run()
