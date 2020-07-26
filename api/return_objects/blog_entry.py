"""The BlogEntry class for the CodeForces API"""

from dataclasses import dataclass


@dataclass
class BlogEntry:
    """https://codeforces.com/apiHelp/objects#BlogEntry"""

    id: int
    original_locale: str
    creation_time_seconds: int
    author_handle: str
    title: str
    content: str  # Can be none
    locale: str
    modification_time_seconds: int
    allow_view_history: bool
    tags: list  # Of strings
    rating: int

    def __eq__(self, other):
        return isinstance(other, BlogEntry) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
