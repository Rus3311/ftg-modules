from .. import loader

from asyncio import sleep 

def register(cb):
	cb(NightMod()) 
	
class NightMod(loader.Module):
	"""НОЧЬ"""
	strings = {'name': 'noch'}
        
	async def snowcmd(self, message):
		"""Используй .noch"""
		await message.edit('🌟⭐🌟⭐🌟🌙🌟⭐🌟⭐🌟\n\n\n\n\n\n🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉')
		await sleep(0.50)
		await message.edit('⭐🌟⭐🌟⭐🌙⭐🌟⭐🌟⭐\n    ✨    ✨     ✨     ✨     ✨   ✨\n\n\n\n\n🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉')
		await sleep(0.50)
		await message.edit('🌟⭐🌟⭐🌟🌙🌟⭐🌟⭐🌟\n    ✨    ✨     ✨     ✨     ✨   ✨\n✨    ✨    ✨    ✨    ✨    ✨       \n\n\n\n🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉')
		await sleep(0.50)
		await message.edit('⭐🌟⭐🌟⭐🌙⭐🌟⭐🌟⭐\n   ✨    ✨     ✨     ✨     ✨   ✨\n✨    ✨    ✨    ✨    ✨    ✨       \n    ✨    ✨    ✨    ✨    ✨    ✨     \n\n\n🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉')
		await sleep(0.50)
		await message.edit('🌟⭐🌟⭐🌟🌙🌟⭐🌟⭐🌟\n    ✨    ✨     ✨     ✨     ✨   ✨\n✨    ✨    ✨    ✨    ✨    ✨       \n    ✨    ✨    ✨    ✨    ✨    ✨     \n✨    ✨    ✨    ✨    ✨    ✨     \n\n🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉')
		await sleep(0.50)
		await message.edit('⭐🌟⭐🌟⭐🌙⭐🌟⭐🌟⭐\n    ✨    ✨     ✨     ✨     ✨   ✨\n✨    ✨    ✨    ✨    ✨     ✨      \n    ✨    ✨    ✨    ✨    ✨    ✨     \n✨    ✨    ✨    ✨    ✨    ✨     \n  ✨      ✨    ✨  ✨      ✨  ✨ \n🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉') 
		await sleep(0.50)
		await message.edit('🌟⭐🌟⭐🌟🌙🌟⭐🌟⭐🌟\n\n✨    ✨    ✨    ✨    ✨    ✨       \n    ✨    ✨    ✨    ✨    ✨    ✨     \n✨    ✨    ✨    ✨    ✨    ✨     \n  ✨      ✨    ✨  ✨      ✨  ✨  \n🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉')
		await sleep(0.50)
		await message.edit('⭐🌟⭐🌟⭐🌙⭐🌟⭐🌟⭐\n\n\n    ✨    ✨    ✨    ✨    ✨    ✨     \n✨    ✨    ✨    ✨    ✨    ✨     \n  ✨      ✨   ✨   ✨      ✨  ✨ \n🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉')
		await sleep(0.50)
		await message.edit('🌟⭐🌟⭐🌟🌙🌟⭐🌟⭐🌟\n\n\n\n✨    ✨    ✨    ✨    ✨    ✨     \n  ✨      ✨    ✨  ✨      ✨  ✨ \n🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉🌉')
		await sleep(0.50)
		await message.edit('\n\n\n\n\n  ✨      ✨    ✨  ✨      ✨  ✨ \nСпокойной ночи🌙')     
