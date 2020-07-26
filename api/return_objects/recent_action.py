"""The RecentAction class for the CodeForces API."""

from dataclasses import dataclass

from api.return_objects.blog_entry import BlogEntry
from api.return_objects.comment import Comment


@dataclass
class RecentAction:
    """https://codeforces.com/apiHelp/objects#RecentAction"""

    time_seconds: int
    blog_entry: BlogEntry
    comment: Comment

