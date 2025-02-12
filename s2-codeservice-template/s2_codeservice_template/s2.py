import asyncio

async def get_message():
	await asyncio.sleep(5)
	return {"message" : "Lumos"}