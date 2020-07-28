"""The User class for the CodeForces API."""

from api.apirequestmaker import strip_dict


class User:
    """https://codeforces.com/apiHelp/objects#User"""

    __slots__ = ["handle", "email", "vlkd", "open_id", "first_name", "last_name", "country", "city", "organization",
                 "contribution", "rank", "rating", "max_rank", "max_rating", "last_online_time_seconds",
                 "registration_time_seconds", "friend_of_count", "avatar", "title_photo"]

    def __init__(self, dic):
        dic = strip_dict(dic)
        self.handle: str = dic["handle"]
        self.email: str = dic.get("email")  # Can be none
        self.vlkd: str = dic.get("vlkd") # Can be none
        self.open_id: str = dic.get("openId")  # Can be none
        self.first_name: str = dic.get("firstName")  # Can be none
        self.last_name: str = dic.get("lastName")  # Can be none
        self.country: str = dic.get("country")  # Can be none
        self.city: str = dic.get("city")  # Can be none
        self.organization: str = dic.get("organization")  # Can be none
        self.contribution: int = dic["contribution"]
        self.rank: str = dic["rank"]
        self.rating: int = dic["rating"]
        self.max_rank: str = dic["maxRank"]
        self.max_rating: int = dic["maxRating"]
        self.last_online_time_seconds: int = dic["lastOnlineTimeSeconds"]
        self.registration_time_seconds: int = dic["registrationTimeSeconds"]
        self.friend_of_count: int = dic["friendOfCount"]
        self.avatar: str = dic["avatar"]
        self.title_photo: str = dic["titlePhoto"]

    def __eq__(self, other):
        return isinstance(other, User) and self.handle == other.handle

    def __ne__(self, other):
        return not self.__eq__(other)
