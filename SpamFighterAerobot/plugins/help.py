from SpamFighterAerobot import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from SpamFighterAerobot import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/4a03839732a7888aa6a55.jpg"

AERO_Help = "**[Aero ✘ Spam Fighter~⟨🇮🇳⟩](https://t.me/SpamFighter_Aerobot)**\n\n"
 
AERO_Help += f"🔰**AVAILABLE COMMAND**🔰\n\n"

AERO_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

AERO_Help += f" /ping - to check ping\n /alive - to check bot alive/version (only main userbot will reply)\n /restart - to restart all spam bots \n /addecho - to addecho \n /rmecho - To remove Echo \n /addsudo - To add sudo user using spam bot \n\n"
 
AERO_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

AERO_Help += f" /leave - to leave public/private channel/groups\n\n"
 
AERO_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

AERO_Help += f" /raid - to raid\n replyraid - to active reply raid\n /dreplyraid - to de-active reply raid\n /spam - this cmd use for Normal spam\n /bigspam - this cmd use for big spam\n /uspam - this cmd use for unlimited Spam until You restart the bots!!\n /delayspam - this cmd use for delay spam\n\n"

AERO_Help += f" /aerospam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"

AERO_Help += f"© @AerodynamicV1_Promotion\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp@SpamFighter_Aerobot(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=AERO_Help,
                                  buttons=[
        [
        Button.url("Channel🔔", "https://t.me/AerodynamicV1_Update"),
        Button.url("Support💬", "https://t.me/AerodynamicV1_Promotion")
        ] 
        ]
        )
