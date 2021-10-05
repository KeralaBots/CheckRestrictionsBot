from pyrogram import Client, __version__, idle
from pyrogram.raw.all import layer

from config import Config


class Bot(Client):
    def __init__(self):
        super().__init__(
            session_name=Config.SESSION_NAME,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=Config.WORKERS,
            plugins=dict(
                root="plugins"
            )
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on @{me.username}.")

    async def stop(self, *args):
        me = await self.get_me()
        await super().stop()
        print(f"@{me.username} stopped. Bye.")
    
    asnyc def idle(self):
        print(f"Idling {me.username}")
        await idle()
