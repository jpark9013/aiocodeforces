import asyncio

from api.api import Client

with open("config.txt", "r") as f:
    key = f.readline()[:-1]
    secret = f.readline()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def main():
    client = Client(key, secret)
    a = await client.get_blog_entries("tmwilliamlin168")
    for blog in a:
        print(blog.title)
    a = await client.get_blog_entry_comments(78777)
    for comment in a:
        print(comment.text)


loop.run_until_complete(main())
loop.close()
