"""The Comment class for the CodeForces API."""

from dataclasses import dataclass


@dataclass
class Comment:
    """https://codeforces.com/apiHelp/objects#Comment"""

    id: int
    creation_time_seconds: int
    commentator_handle: str
    locale: str
    text: str
    parent_comment_id: int  # Can be none
    rating: int

    def __eq__(self, other):
        return isinstance(other, Comment) and self.id == other.id
