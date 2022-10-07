
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from SpamFighterAerobot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

AEROBOTZ_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/8fa034b5a6faae2c9da16.jpg"


AERO_Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/AerodynamicV1_Update"),
        Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/AerodynamicV1_Promotion")
        ],
        [
        Button.url("Network", "https://t.me/AerodynamicV1Botz")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[𝘼𝙚𝙧𝙤𝙙𝙮𝙣𝙖𝙢𝙞𝙘𝙑1](tg://user?id={OWNER_ID})"
        creator = f"[𝙑𝙧𝙖𝙟𝙚𝙨𝙝](tg://user?id={5708737143})"
        AERO_ON = f"""
ʜᴇʏ {mention},
ᴛʜɪs ɪs SpamFighterAerobot ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- {creator}!

ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ:- {myOwner}

ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ:- {creator}

ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ Network!
    """
        await e.client.send_file(e.chat_id, AEROBOTZ_IMG, caption=AERO_ON, buttons=AERO_Button)
