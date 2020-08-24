from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd("anna"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    #input_str = event.pattern_match.group(1)

   # if input_str == "fuk":

    await event.edit("❤️ ANNA TE AMOOOOO ❤️")

    animation_chars = [

            "👸🏼 MI REINAAAAA 👸🏼",

            "💞 TE QUIEROOOOO 💞",

            "❤️ ANNA TE AMOOOOO ❤️",

            "👸🏼 MI REINAAAAA 👸🏼",
            
            "💞 TE QUIEROOOOO 💞",

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])
