from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils


def register(cb):
	cb(CutMod())


class Lines50Mod(loader.Module):
	"""Cut music with 50 lines via @audiocutterbot"""

	strings = {'name': 'audiocutter'}

	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()

	async def linescmd(self, message):
		""".cut <reply to music>"""
		
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("reply to music")
			return
		try:
			photo = reply.media.photo
		except:
			await message.edit("reply to music only")
			return
		
		
				
				
		chat = '@audiocutterbot'
		await message.edit('... <code>in process...</code>')
		async with message.client.conversation(chat) as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True, from_users=438382295))
				
				await message.client.send_file(chat, music)
				
				response = await response
			except YouBlockedUserError:
				await message.reply('<code>Unblock</code> @audiocutterbot')
				return

			await message.delete()
			await message.client.send_file(message.to_id, response.media)
			
