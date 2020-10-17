import re
import logging
from pyrogram import filters
from pyrogram.types import Message
from bot import Bot


@Bot.on_message(filters.text & filters.private & filters.incoming)
async def private_check(c: Bot, m: Message):
    if bool(re.search(r"\d", m.text)) is True:
        c_id = int(m.text)
    else:
        c_id = m.text
    try:
        a = await c.get_chat(c_id)
        if a.title is not None:
            full_id = a.id
            str_chat = f"{full_id}"
            chat_id = str_chat[4:]
            chat_name = a.title
            link = f"https://t.me/c/{chat_id}/2"
            print(link)
        else:
            chat_id = a.id
            chat_name = a.first_name
            link = f"tg://user?id={chat_id}"
            print(link)

    except Exception as e:
        await c.send_message(
            m.chat.id,
            f"The given Username/Userid {c_id} is not valid",
            reply_to_message_id=m.message_id
        )
        logging.error(e)
        return

    try:
        if a.restrictions is not None:
            text = f"[{chat_name}]({link}) has the following restriction_reason(s):\n"
            lat = "ℹ️ Powered by @KeralasBots"
            for i in a.restrictions:
                v_text = f"👉🏻 {i.reason}-{i.platform}: {i.text}\n\n"
                text += "{}".format(v_text)
            await c.send_message(
                m.chat.id,
                text + lat,
                parse_mode="markdown",
                reply_to_message_id=m.message_id
            )
        else:
            await c.send_message(
                m.chat.id,
                f"Good News! No Limitations are currently applied to [{chat_name}]({link})\n\nℹ️ Powered by @KeralasBots",
                parse_mode='markdown',
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
