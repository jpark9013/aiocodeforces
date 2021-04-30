class RatingChange:

    __slots__ = ["contest_id", "contest_name", "handle", "rank", "rating_update_time_seconds", "old_rating",
                 "new_rating"]

    def __init__(self, dic):
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
