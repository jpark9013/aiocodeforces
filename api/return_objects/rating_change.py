"""The RatingChange class for the CodeForces API."""

from api.apirequestmaker import strip_dict


class RatingChange:
    """
    Represents a rating change on CodeForces.

    ..container:: operations

        ..describe:: x == y

            Checks if two RatingChanges are equal.

        ..describe: x != y

            Checks if two RatingChanges are not equal.

    Attributes
    -----------
    contest_id: :class:``int``
        The ID of the contest for the RatingChange.
    contest_name: :class:``str``
        The name of the contest for the RatingChange.
    handle: :class:``str``
        The handle of the user for the RatingChange.
    rank: :class:``int``
        The place of the user in the contest. Will not update after further rank change.
    rating_update_time_seconds: :class:``int``
        Time when rating was updated for the contest, in UNIX format.
    old_rating: :class:``int``
        The user's old rating.
    new_rating: :class:``int``
        The user's new rating.
    """

    __slots__ = ["contest_id", "contest_name", "handle", "rank", "rating_update_time_seconds", "old_rating",
                 "new_rating"]

    def __init__(self, dic):
        dic = strip_dict(dic)
        self.contest_id: int = dic["contestId"]
        self.contest_name: str = dic["contestName"]
        self.handle: str = dic["handle"]
        self.rank: int = dic["rank"]
        self.rating_update_time_seconds: int = dic["ratingUpdateTimeSeconds"]
        self.old_rating: int = dic["oldRating"]
        self.new_rating: int = dic["newRating"]

    def __eq__(self, other):
        return isinstance(other, RatingChange) and self.contest_id == other.contest_id and self.handle == other.handle

    def __ne__(self, other):
        return not self.__eq__(other)
