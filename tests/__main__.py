import asyncio

from api.api import Client

with open("config.txt", "r") as f:
    key = f.readline()
    secret = f.readline()

loop = asyncio.new_event_loop()
client = Client(key, secret)


async def main():
    a = await client.get_blog_entries("tmwilliamlin168")
    for blog in a:
        print(a.title)
    a = await client.get_blog_entry_comments(78777)
    for comment in a:
        print(a.text)

loop.run_until_complete(main())

