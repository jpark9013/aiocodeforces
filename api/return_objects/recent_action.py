"""The RecentAction class for the CodeForces API."""


from api.apirequestmaker import strip_dict
from api.return_objects.blog_entry import BlogEntry
from api.return_objects.comment import Comment


class RecentAction:
    """https://codeforces.com/apiHelp/objects#RecentAction"""

    __slots__ = ["time_seconds", "blog_entry", "comment"]

    def __init__(self, dic):
        strip_dict(dic)
        self.time_seconds: int = dic["timeSeconds"]
        self.blog_entry: BlogEntry = BlogEntry(dic.get("blogEntry")) if dic.get("blogEntry") else None
        self.comment: Comment = Comment(dic.get("comment")) if dic.get("comment") else None

