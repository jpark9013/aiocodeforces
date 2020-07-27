"""The RecentAction class for the CodeForces API."""


from api.return_objects.blog_entry import BlogEntry
from api.return_objects.comment import Comment


class RecentAction:
    """https://codeforces.com/apiHelp/objects#RecentAction"""

    def __init__(self, dic):
        self.time_seconds: int = dic["timeSeconds"]
        self.blog_entry: BlogEntry = BlogEntry(dic["blogEntry"])
        self.comment: Comment = Comment(dic["comment"])

