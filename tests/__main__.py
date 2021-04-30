import asyncio

from aiocodeforces.client import Client

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
    a = await client.get_recent_actions()
    for i in a:
        try:
            print(i.blog_entry.content)
            print(i.comment.text)
        except AttributeError:
            print("No attribute text")
    a = await client.get_contest_list()
    for i in a:
        print(i.name)
    print(await client.get_friends(only_online=True))
    await client.close()

loop.run_until_complete(main())
