import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot


@Bot.on_message(filters.regex('(?i)@(s)?'))
async def check(c: Client, m: Message):
    c_id = m.text
    user_input = f"{c_id}"
    try:
        a = await c.get_chat(user_input)
        if a.title is not None:
            full_id = a.id
            str_chat = f"{full_id}"
            chat_id = str_chat[4:]
            chat_name = a.title
            link = f"https://t.me/c/{chat_id}/2"
        else:
            chat_id = a.id
            chat_name = a.first_name
            link = f"tg://user?id={chat_id}"

    except Exception as e:
        await c.send_message(
            m.chat.id,
            f"The given Username {c_id} is not valid",
            reply_to_message_id=m.message_id
        )
        logging.error(e)
        return
    try:
        text = f"[{chat_name}]({link}) has the following restriction_reason(s):\n"
        lat = "ℹ️ Powered by @KeralasBots"
        for i in a.restrictions:
            v_text = f"👉🏻 {i.reason}-{i.platform}: {i.text}\n\n"
            text += "{}".format(v_text)
        await c.send_message(
            m.chat.id,
            text+lat,
            parse_mode="markdown",
            reply_to_message_id=m.message_id
        )

    except Exception as e:
        await c.send_message(
            m.chat.id,
            f"Good News! No Limitations are currently applied to [{chat_name}]({link})\n\nℹ️ Powered by @KeralasBots",
            parse_mode='markdown',
            reply_to_message_id=m.message_id
        )
        logging.warning(e)
