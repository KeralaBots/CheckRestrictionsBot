import logging
from pyrogram import Client
from config import Config


BOT = Client(
    "CheckRestrictionsBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(
        root="plugins"
    )
)
if __name__ == "__main__":
    BOT.run()
