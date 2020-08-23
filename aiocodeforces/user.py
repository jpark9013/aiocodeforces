"""The User class for the CodeForces API."""


class User:
    """
    Represents a user on CodeForces.

    ..container:: operations

        ..describe:: x == y

            Checks if two Users are equal.

        ..describe: x != y

            Checks if two Users are not equal.

    Attributes
    -----------
    handle: :class:``str``
        The handle of the User.
    email: :class:``str``
        The email of the User. Can be ``None``.
    vlkd: :class:``str``
        User ID for VK social network. Can be ``None``.
    open_id: :class:``str``
        User's open ID. Can be ``None``.
    first_name: :class:``str``
        User's first name. Can be ``None``.
    last_name: :class:``str``
        User's last name. Can be ``None``.
    country: :class:``str``
        User's country. Can be ``None``.
    city: :class:``str``
        User's city. Can be ``None``.
    organization: :class:``str``
        User's organization. Can be ``None``.
    contribution: :class:``int``
        User's contribution.
    rank: :class:``str``
        User's rank.
    rating: :class:``int``
        User's rating.
    max_rank: :class:``str``
        User's max rank (not necessarily equivalent to current rank).
    max_rating: :class:``int``
        User's max rating (not necessarily equivalent to current rating).
    last_online_time_seconds: :class:``int``
        Time when user was last seen, in UNIX format.
    registration_time_seconds: :class:``int``
        Time when user registered, in UNIX format.
    friend_of_count: :class:``int``
        Amount of friends the user has.
    avatar: :class:``str``
        The user's avatar URL.
    title_photo: :class:``str``
        The user's title photo URL.
    """

    __slots__ = ["handle", "email", "vlkd", "open_id", "first_name", "last_name", "country", "city", "organization",
                 "contribution", "rank", "rating", "max_rank", "max_rating", "last_online_time_seconds",
                 "registration_time_seconds", "friend_of_count", "avatar", "title_photo"]

    def __init__(self, dic):
        self.handle: str = dic["handle"]
        self.email: str = dic.get("email")  # Can be none
        self.vlkd: str = dic.get("vlkd")  # Can be none
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
