import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from SilentRobot.events import register
from SilentRobot import telethn as borg, OWNER_ID, OWNER_NAME
from SilentRobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/653cc589cef8ce310a9f2.jpg"
file2 = "https://te.legra.ph/file/653cc589cef8ce310a9f2.jpg"
file3 = "https://te.legra.ph/file/653cc589cef8ce310a9f2.jpg"
file4 = "https://te.legra.ph/file/653cc589cef8ce310a9f2.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Silent = f"• **Hey [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'm Silent**\n"
    Silent += f"• **My Uptime** - `{uptime}`\n"
    Silent += f"• **Telethon Version** - `{version.__version__}`\n"
    Silent += f"• **PTB Version** - `{telegram.__version__}`\n"
    Silent += f"• **Pyrogram Version** - `{pyro}`\n"
    Silent += f"• **My Master** - [Xelcius](tg://user?id={OWNER_ID})\n\n"
    Silent += f"Thanks For Adding Me In {yes.chat.title}"
    BUTTON = [[Button.url("Support Chat", "https://t.me/SilentSupport"), Button.url("Updates", "https://t.me/Galaxia_Update")]]
    on = await borg.send_file(yes.chat_id, file="https://te.legra.ph/file/653cc589cef8ce310a9f2.jpg",caption=Silent, buttons=BUTTON)

@register(pattern=("/repo"))
async def repo(event):
    Silent = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), Click The Button Below To Get My Repo**\n\n"
    BUTTON = [[Button.url("GitHub", "https://github.com/Wolf2901/SilentRobot"), Button.url("Developer", "https://t.me/Silent_Smile_04")]]
    await borg.send_file(event.chat_id, file="https://te.legra.ph/file/653cc589cef8ce310a9f2.jpg", caption=Silent, buttons=BUTTON)
