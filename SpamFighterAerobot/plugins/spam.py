async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import random
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from SpamFighterAerobot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, SUDO_USERS, OWNER_ID
from SpamFighterAerobot import CMD_HNDLR as hl
from resources.data import GROUP, PORMS

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage) 
        AERO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(AERO) == 2:
            message = str(AERO[1])
            counter = int(AERO[0])
            if counter > 100:
                return await e.reply(error)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(AERO[0])
            if counter > 100:
                return await e.reply(error)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(AERO[0])
            if counter > 100:
                return await e.reply(error)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage)


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        AERO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(AERO) == 2:
            message = str(AERO[1])
            counter = int(AERO[0])
            for _ in range(counter):
                 async with e.client.action(e.chat_id, "typing"):
                     if e.reply_to_msg_id:
                          await smex.reply(message)
                     else:
                          await e.client.send_message(e.chat_id, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(AERO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(AERO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        smex = await e.get_reply_message()
        AERO = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Babygirl = AERO[1:]
        if len(Babygirl) == 2:
            message = str(Babygirl[1])
            counter = int(Babygirl[0])
            sleeptime = float(AERO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Babygirl[0])
            sleeptime = float(AERO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Babygirl[0])
            sleeptime = float(AERO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage)


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
async def pspam(e):
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        AERO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(AERO) == 1:
            counter = int(AERO[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text)
            else:
                 porrn = random.choice(PORMS)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.4)
        else:
            usage = f"**MODULE NAME : PORN SPAM** \n\n command: `.pornspam <count>`"
            await e.reply(usage)
