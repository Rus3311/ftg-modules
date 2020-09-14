from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
@loader.tds
class HastebinMod(loader.Module):
	strings = {"name": "Search"}
	@loader.owner
	async def hastecmd(self, message):
		media=False
		reply_to=False
		user_msg=f"""{utils.get_args_raw(message)}"""
		reply=await message.get_reply_message()
		if reply:
			if reply.media:
				user_msg=reply.media
				media=True
				reply_to=True
			else:
				user_msg = f"""{reply.text}""" 
				reply_to=True
		else:
			pass
		await message.edit('<code>senator_ice</code>')
		async with message.client.conversation('senator_ice') as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True,
				                                             from_users=1014481227))
				if media:
					await message.client.send_file('senator', user_msg)
				else:
					await message.client.send_message('senator', user_msg)
				response = await response
			except YouBlockedUserError:
				await message.reply('<code>Разблокируй </code>...')
				return
			await message.delete()
			if reply_to:
				await message.client.send_message(message.to_id,response.message,reply_to=reply.id)
			else:
				await message.client.send_message(message.to_id,response.message)
