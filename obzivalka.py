from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.kus", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit("Слышь")
    await asyncio.sleep(1)
    await event.edit("Ты")
    await asyncio.sleep(1)
    await event.edit("Долбаеб")
    await asyncio.sleep(1)
    await event.edit("Волшебое мудило")
    await asyncio.sleep(1)
    await event.edit("Ушлёпок феминизма")
    await asyncio.sleep(1)
    await event.edit("Ёбнутый пингвин")
    await asyncio.sleep(1)
    await event.edit("Хуёвый сказочник")
    await asyncio.sleep(1)
    await event.edit("Ёбаная доска")
    await asyncio.sleep(1)
    await event.edit("Дурка хуйни")
    await asyncio.sleep(1)
    await event.edit("Дятел на хуе")
    await asyncio.sleep(1)
    await event.edit("Чмошник")
    await asyncio.sleep(1)
    await event.edit("Яйцеглот профессиональный")
    await asyncio.sleep(1)
    await event.edit("Пососательница Путина")
    await asyncio.sleep(1)
    await event.edit("Короче")
    await asyncio.sleep(1)
    await event.edit("Иди нахуй")
    await asyncio.sleep(1)
    await event.edit("🌚🤝")





