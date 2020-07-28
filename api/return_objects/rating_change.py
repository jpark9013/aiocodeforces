"""The RatingChange class for the CodeForces API."""

from api.apirequestmaker import strip_dict


class RatingChange:
    """https://codeforces.com/apiHelp/objects#RatingChange"""

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
