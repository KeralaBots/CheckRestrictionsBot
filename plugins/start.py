from pyrogram import Client, filters


@Client.on_message(filters.command("start"))
async def start(c, m):
    await c.send_message(
        m.chat.id,
        f"Hi {m.from_user.first_name}. I am an account info checker inspired by @SpEcHIDe 's @CheckRestrictionsBot."\
        " Send me the username of the USERS/GROUPS/CHANNELS/BOTS to check for any applied Telegram restrictions!"\
        "\n\n<code>Example : @username</code>.\n\nMade with ❤️ by @KeralasBots",
        parse_mode="html"
    )
