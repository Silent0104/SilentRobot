import asyncio

from asyncio import sleep
from telethon import events
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins

from SilentRobot import telethn, OWNER_ID, DEV_USERS, DRAGONS, DEMONS

# =================== CONSTANT ===================

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

OFFICERS = [OWNER_ID] + DEV_USERS + DRAGONS + DEMONS

# Check if user has admin rights

async def is_administrator(user_id: int, message):
    admin = False
    async for user in telethn.iter_participants(
        message.chat_id, filter=ChannelParticipantsAdmins
    ):
        if user_id == user.id or user_id in OFFICERS:
            admin = True
            break
    return admin


@telethn.on(events.NewMessage(pattern="^[!/]zombies ?(.*)"))
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**πΆππππ π²ππππ, 0 πππππππ πππππππ πππππ.**"
    if con != "clean":
        kontol = await show.reply("`πππππππππ π΅ππ π³ππππππ π°πππππ ππ πΊπππ ππππ...`")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = (
                f"**πππππππππ...** `{del_u}` **π³ππππππ π°ππππππ πΈπ ππππ πΆππππ,"
                "\nπ²ππππ πΈπ ππππ π²ππππππ** `/zombies clean`"
            )
        return await kontol.edit(del_status)
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await show.reply("**π±πππππππ π°ππππ π½πππ π·π π°ππππ πΌππ π±ππππ!**")
    memek = await show.reply("`π³ππππππ π°ππππππ π±ππππ πΊπππππ...`")
    del_u = 0
    del_a = 0
    async for user in telethn.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                return await show.edit("`π½ππ π·πππ π° πΆππππ π±ππ πππππ`")
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await telethn(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1
    if del_u > 0:
        del_status = f"**π²ππππππ** `{del_u}` **πππππππ**"
    if del_a > 0:
        del_status = (
            f"**π²ππππππ** `{del_u}` **πππππππ** "
            f"\n`{del_a}` **π³ππππππ π°ππππππ ππππ π²πππππππππ π½ππ πΊπππππ.**"
        )
    await memek.edit(del_status)
        
from telethon.tl.types import UserStatusLastMonth, UserStatusLastWeek, ChatBannedRights
from SilentRobot.events import register
from telethon import *
from telethon.tl.functions.channels import (EditBannedRequest)
                                            

@register(pattern="^/banall")
async def _(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not event.chat.admin_rights.ban_users:
        return
    if not admin and not creator:
        await event.reply("πΈ π°π π½ππ π°ππππ π·πππ!")
        return
    c = 0
    KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)
    await event.reply("πππππππππ πΏππππππππππ π»πππ...")
    async for i in event.client.iter_participants(event.chat_id):

        if isinstance(i.status, UserStatusLastMonth):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1
                    
        if isinstance(i.status, UserStatusLastMonth):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1                    

    required_string = "ππππππππππππ’ ππππππ **{}** πππππ"
    await event.reply(required_string.format(c))
   
