# aiocodeforces

Async based API wrapper for CodeForces written in Python for Python.

Currently a work in progress. 

Documentation is also being worked on right now.


Example usage:
```py
import asyncio

from aiocodeforces.client import Client


loop = asyncio.get_event_loop()
client = Client()

async def main():
    a = await client.get_blog_entries("jpark9013")
    for blog in a:
        print(blog.title)
        
    a = await client.get_blog_entry_comments(82127)
    for comment in a:
        print(comment.text)
        
    a = await client.get_recent_actions()
    for i in a:
        try:
            print(i.blog_entry.content)
            print(i.comment.text)
            
        except AttributeError
            print("No attribute text")
            
    a = await client.get_contest_list()
    for i in a:
        print(i.name)
        
    await client.close()

loop.run_until_complete(main())
```

