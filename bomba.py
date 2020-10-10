from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.fakelove", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit("🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n")
    await asyncio.sleep(1)
    await event.edit("🌊Я!🍷🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n")
    await asyncio.sleep(1)
    await event.edit("🌊🌊🌊🌊 \n🌊ТЕБЯ🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n")
    await asyncio.sleep(1)
    await event.edit("🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊LOVE🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n")
    await asyncio.sleep(1)
    await event.edit("🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊MY🌪️🌊 \n🌊🌊🌊🌊 \n")
    await asyncio.sleep(1)
    await event.edit("🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊🌊🌊🌊 \n🌊SOUL🌊 \n")
    await asyncio.sleep(1)
    await event.edit("❤️💛💚💙 \n💜🖤💙💚 \n💛❤️💚💙 \n💜🖤💙💚 \n💛❤️💚💙 \n")
    await asyncio.sleep(1)
    await event.edit("🖤💜💙💚 \n💛❤️💚💙 \n💜🖤💙💚 \n💛❤️💚💙 \n💜🖤💙💚 \n")
    await asyncio.sleep(1)
    await event.edit("❤️💛💚💙 \n💜🖤💙💚 \n💛❤️💚💙 \n💜🖤💙💚 \n💛❤️💚💙 \n")
    await asyncio.sleep(1)
    await event.edit("🖤💜💙💚 \n💛❤️💚💙 \n💜🖤💙💚 \n💛❤️💚💙 \n💜🖤💙💚 \n")
    await asyncio.sleep(1)
    await event.edit("Вот и мифу конец🥃")
