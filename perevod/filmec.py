from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils


def register(cb):
	cb(VKMMod())


class Lines50Mod(loader.Module):
	"""Find music via @vkm_bot"""

	strings = {'name': 'vkm_bot'}

	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()

	async def linescmd(self, message):
		""".muz <text>"""
		
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("text")
			return
		try:
			photo = reply.media.photo
		except:
			await message.edit("text")
			return
		
		
				
				
		chat = '@vkm_bot'
		await message.edit('@vkm_bot <code>in process...</code>')
		async with message.client.conversation(chat) as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True, from_users=1120861844))
				
				await message.client.send_file(chat, photo)
				
				response = await response
			except YouBlockedUserError:
				await message.reply('<code>Unblock</code> @vkm_bot')
				return

			await message.delete()
			await message.client.send_file(message.to_id, response.media)
			
