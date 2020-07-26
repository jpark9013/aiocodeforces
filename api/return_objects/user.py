"""The User class for the CodeForces API."""

from dataclasses import dataclass


@dataclass
class User:
    """https://codeforces.com/apiHelp/objects#User"""

    handle: str
    email: str  # Can be none
    vlkd: str  # Can be none
    open_id: str  # Can be none
    first_name: str  # Can be none
    last_name: str  # Can be none
    country: str  # Can be none
    city: str  # Can be none
    organization: str  # Can be none
    contribution: int
    rank: str
    rating: int
    max_rank: str
    max_rating: int
    last_online_time_seconds: int
    registration_time_seconds: int
    friend_of_count: int
    avatar: str
    title_photo: str

    def __eq__(self, other):
        return isinstance(other, User) and self.handle == other.handle

    def __ne__(self, other):
        return not self.__eq__(other)
