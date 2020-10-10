from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.fakelove", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️Я!▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \nТЕБЯ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \nLOVE \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️MY▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \nSOUL \n")
    await asyncio.sleep(1)
    await event.edit("❤️💛💚💙 \n💜🖤💙💚 \n💛❤️💚💙 \n💜🖤💙💚 \n💛❤️💚💙 \n")
    await asyncio.sleep(0.5)
    await event.edit("🖤💜💙💚 \n💛❤️💚💙 \n💜🖤💙💚 \n💛❤️💚💙 \n💜🖤💙💚 \n")
    await asyncio.sleep(0.5)
    await event.edit("Вот и мифу конец!")
