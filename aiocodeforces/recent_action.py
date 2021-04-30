from aiocodeforces.blog_entry import BlogEntry
from aiocodeforces.comment import Comment


class RecentAction:

    __slots__ = ["time_seconds", "blog_entry", "comment"]

    def __init__(self, dic):
        self.time_seconds: int = dic["timeSeconds"]
        self.blog_entry: BlogEntry = BlogEntry(dic.get("blogEntry")) if dic.get("blogEntry") else None
        self.comment: Comment = Comment(dic.get("comment")) if dic.get("comment") else None

