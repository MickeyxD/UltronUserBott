import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from telethon import version
from userbot import ALIVE_NAME, StartTime, ULTRONversion
from ULTRONBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from . import *
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "✞︎t͛ẞ̸ 𝖑𝖊ɠêɳ̃dẞø✞︎ 🇮🇳"
ULTRON_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ℓєgєи∂ Choice 𝖑𝖊ɠêɳ̃dẞø✞︎"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@Legend_Userbot"

Legend = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={Legend})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="legend$"))
@bot.on(sudo_cmd(pattern="legend$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  ULTRON_IMG:
        ULTRON_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        
        ULTRON_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        ULTRON_caption += f"        **♥ẞø† ẞ✞︎α†µѕ** \n"
        ULTRON_caption += f"•⚜️• **Øաղ̃ҽ̈ɾ**          : {mention}\n\n"
        ULTRON_caption += f"•📍• **𝖑𝖊ɠêɳ̃dẞø†**   : {ULTRONversion}\n"
        ULTRON_caption += f"•📍• **†ҽ̀lҽ́ƭhøղ̃**     : `{version.__version__}`\n"
        ULTRON_caption += f"•📍• **𝚄ρƭเɱε**         : `{uptime}`\n"
        ULTRON_caption += f"•📍• **𝙶𝚛𝚘𝚞𝚙**           : [𝙶𝚛𝚘𝚞𝚙](t.me/Legend_Userbot)\n"
        ULTRON_caption += f"•📍• **𝙼𝚢 𝙶𝚛𝚘𝚞𝚙**  : {CUSTOM_YOUR_GROUP}\n"   

        await alive.client.send_file(
            alive.chat_id, ULTRON_IMG, caption=ULTRON_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         𝕭𝖔𝖙 𝕾𝖙𝖆𝖙𝖚𝖘\n"
            f"•⚡• 𝕿єℓєτнοи    : `{version.__version__}`\n"
            f"🇮🇳 ℓєgєи∂ϐοτ  : `{ULTRONversion}`\n"
            f"🇮🇳 υρτιмє        : `{uptime}`\n"
            f"🔱 ɱαรƭεɾ        : {mention}\n"
            f"🔱 σωɳεɾ         : [ℓєgєи∂](t.me/Its_M1CKEY0P)\n"
        )


msg = f"""
**  ⚜️ Lêɠêɳ̃dẞø† ιѕ σиℓιиє ⚜️**

{Config.ALIVE_MSG}

**    ♥️ ẞø✞︎ ẞ✞︎α✞︎µѕ ♥️**
**•⚜️•Øաղ̃ҽ̈r     :** **{mention}**

**•🌹•𝖑𝖊ɠêɳ̃dẞø✞︎ :** {ULTRONversion}
**•🌹•✞︎ҽ̀lҽ́ƭhøղ  :** {version.__version__}
**•🌹•Ãbûßê     :**  {abuse_m}
**•🌹•ßudø      :**  {is_sudo}
**
"""
botname = Config.BOT_USERNAME

@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def legend_a(event):
    try:
        legend = await bot.inline_query(botname, "alive")
        await legend[0].click(event.chat_id)
        if event.sender_id == Its_M1CKEY0P:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)

CmdHelp("botstats").add_command(
    'bot', None, 'υѕє αи∂ ѕєє'
).add()
