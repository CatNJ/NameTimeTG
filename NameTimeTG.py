import time
import config

from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

client = TelegramClient("anon", config.API_ID, config.API_HASH)


async def main():
	last_time_string = ''

	while True:
		local_time = time.localtime()
		time_string = time.strftime("%H:%M", local_time)
		time.sleep(1)

		if time_string != last_time_string:
			await client(UpdateProfileRequest(first_name=f"⏰ {time_string}"))	# name
			last_time_string = time_string


			
with client:
	while True:
		client.loop.run_until_complete(main())
		time.sleep(15)
