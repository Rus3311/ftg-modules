#made by @VadimSap & KeyZenD
import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.blya(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`СЛЫШЬ`")
	await asyncio.sleep(0.5)
	await typew.edit("`ТЫ`")
	await asyncio.sleep(0.5)
	await typew.edit("`рл`")
	await asyncio.sleep(0.5)
        await typew.edit("`Логов больше нет!`")






