import asyncio
from collections import deque
from . import *

@bot.on(admin_cmd(pattern=r"^π€¬", outgoing=True))
@bot.on(sudo_cmd(pattern=r"^π€¬", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "πΈ ππ πππππ’ ")
    deq = deque(list("π‘π₯π‘π₯π€¬π₯π€¬π₯π€¬π2.πΎπ₯π‘π₯π€¬π‘π₯π€¬π€¬π₯π‘"))
    for _ in range(100):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)
        
CmdHelp("angry").add_command(
  "π€¬", None, "ΟΡΡ Ξ±ΠΈβ ΡΡΡ"
).add()
