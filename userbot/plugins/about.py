from . import *
import asyncio
import random
from telethon import events
from ULTRONBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ULTRON"

# Thanks to ULTRON BRO.. 
# animation Idea by @M1CKEY_0P (op coder)
# Kang with credits else gay...
# alive.py for

edit_time = 5
""" =======================CONSTANTS====================== """
file1="https://telegra.ph/file/2d41a6b1b3713579c63c2.jpg"
file2="https://telegra.ph/file/9fb5502699714b8eabca3.jpg"
file3="https://telegra.ph/file/f04dcb487d52b97c36a54.jpg"
file4="https://telegra.ph/file/bac71ea81bebea8332f86.jpg"
file5="https://telegra.ph/file/56330a785e4f2a5919e1c.jpg"""" =======================CONSTANTS====================== """
pm_caption = "**π₯γLΓͺΙ ΓͺΙ³ΜdαΊΓΈβ γπ₯**\n\n"
pm_caption += "ππ **ππ¨π,πππ πππ ππππππππ , πππ ππΊππΎ πΌπΊππΎ ππΏ ππ π»πΎππππΎ .. πππππππ πππ ππΎππ πππΌππ«π.**ππ\n\n"
pm_caption += "ΰΌΰΌππΉπ¬ππππ πΈπ \n\n"
pm_caption += "π«π«**βοΈtΝαΊΜΈ LΓͺΙ ΓͺΙ³ΜdαΊΓΈβ **π«π« >>γ V2.O\n"
pm_caption += "ππ**ππΙ ΓͺΙ³Μd**ππ   >>γ [ΞΏΟΠΈΡΡ](https://t.me/Its_M1CKEY0P)\n"
pm_caption += f"π°π°**πΈππππ**π°π°  >>γ {legend_mention}\n"
pm_caption += "β£β£ **ππΙ ΓͺΙ³ΜdαΊΓΈβοΈ**β£β£ >>γ [π²πΞΏΟΟ](https://t.me/Legend_Userbot)\n\n"
pm_caption += "ππ **π½ππΞΏ**ππ  >>γ [π½ΡΟΞΏ](https://github.com/ULTRON-OS/ULTRONBOT)\n\n"
pm_caption += "[....βββββββββ\n....βββββββββ\n.......ββββ£πΉπ«ππ«πΉβ£ββββ\n...............βββ\n](https://t.me/Its_M1CKEY0P)\n\n"
@borg.on(admin_cmd(pattern=r"abot"))
@bot.on(sudo_cmd(pattern="abot$", allow_sudo=True))
async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)
    
    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
    CmdHelp("abot").add_command(
      'abot', None , 'BEST alive command'
).add()
