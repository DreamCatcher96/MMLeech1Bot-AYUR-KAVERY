#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging

import pyrogram
from tobrot import *

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            f"""<b>🙋🏻‍♂️ Hello dear!\n\n🤖 This Is A Leech Bot, Exclusively Made For Team #MALLUMOVIES\nThis Group Is Not Supposed To Use Me, Please Contact My Boss!</b>\n\n<b>YOUR GROUP ID : 👇</b> <code>{message.chat.id}</code>""",
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🤖 MY BOSS 👤', url='https://t.me/WhitE_Devil09')
                    ]
                ]
               )
            )
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    if UPLOAD_AS_DOC:
        utxt = "Document"
    else:
        utxt = "Streamable"
    await message.reply_text(
        """<b>Hello 👋 This is TorrentleechBot 🤖\n\nⓂ️ Exclusively Made For Team #MalluMovies 😍</b>""",
        disable_web_page_preview=True,
    )
