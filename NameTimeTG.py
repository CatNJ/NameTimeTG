import time

from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest


api_id = 12345678	# your api_id
api_hash = "h64m92mkjsciuvyg47sdjvbjht4h"	# your api_hash
client = TelegramClient("anon", api_id, api_hash)


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
