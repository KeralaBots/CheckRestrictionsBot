from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot


@Bot.on_message(filters.command("start"))
async def start(c: Client, m: Message):
    await c.send_message(
        m.chat.id,
        f"Hi {m.from_user.first_name}. I am an account info checker inspired by @SpEcHIDe 's @CheckRestrictionsBot."\
        " Send me the username of the USERS/GROUPS/CHANNELS/BOTS to check for any applied Telegram restrictions!"\
        "\n\n<code>Example : @username</code>.\n\nMade with ❤️ by @KeralasBots",
        parse_mode="html"
    )
