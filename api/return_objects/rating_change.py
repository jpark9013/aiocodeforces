"""The RatingChange class for the CodeForces API."""

from dataclasses import dataclass


@dataclass
class RatingChange:
    """https://codeforces.com/apiHelp/objects#RatingChange"""

    contest_id: int
    contest_name: str
    handle: str
    rank: int
    rating_update_time_seconds: int
    old_rating: int
    new_rating: int

    def __eq__(self, other):
        return isinstance(other, RatingChange) and self.contest_id == other.contest_id and self.handle == other.handle

    def __ne__(self, other):
        return not self.__eq__(other)
