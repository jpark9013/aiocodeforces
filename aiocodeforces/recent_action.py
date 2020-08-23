"""The RecentAction class for the CodeForces API."""


from aiocodeforces.blog_entry import BlogEntry
from aiocodeforces.comment import Comment


class RecentAction:
    """
    Represents a recent action on CodeForces.

    Attributes
    -----------
    time_seconds: :class:``int``
        The time, in UNIX format, of the recent action.
    blog_entry: :class:``BlogEntry``
        The Blog Entry submission. Can be ``None``.
    comment: :class:``Comment``
        The comment submission. Can be ``None``.
    """

    __slots__ = ["time_seconds", "blog_entry", "comment"]

    def __init__(self, dic):
        self.time_seconds: int = dic["timeSeconds"]
        self.blog_entry: BlogEntry = BlogEntry(dic.get("blogEntry")) if dic.get("blogEntry") else None
        self.comment: Comment = Comment(dic.get("comment")) if dic.get("comment") else None

