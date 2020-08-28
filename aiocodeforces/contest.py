"""The Contest class for the CodeForces API."""

from aiocodeforces.enum import ContestPhase, ContestType


class Contest:
    """Represents a CodeForces Contest.

    ..container:: operations

        ..describe:: x == y

            Checks if two Contests are equal.

        ..describe:: x != y

            Checks if two Contests are not equal.

    Attributes
    -----------
    id: :class:``int``
        The ID of the Contest.
    name: :class:``str``
        The name of the Contest.
    type: :class:``ContestType``
        The type of the Contest.
    phase: :class:``ContestPhase``
        The phase of the Contest.
    frozen: :class:``bool``
        Whether the Contest is frozen or not.
    duration_seconds: :class:``int``
        The duration of the Contest, in seconds.
    start_time_seconds: :class:``int``
        The start time of the Contest, in seconds. Can be ``None``.
    relative_time_seconds: :class:``int``
        The number of seconds passed after Contest start. Can be ``None``.
    prepared_by: :class:``str``
        The handle of the user whom the Contest was prepared by. Can be ``None``.
    website_url: :class:``str``
        URL for contest-related website. Can be ``None``.
    description: :class:``str``
        Description of the Contest. Can be ``None``.
    difficulty: :class:``int``
        The difficulty of the Contest, from 1 to 5; larger means more difficult. Can be ``None``.
    kind: :class:``str``
        The type of Contest. It's one from the following categories: Official ICPC Contest, Official School Contest,
        Opencup Contest, School/University/City/Region Championship, Training Camp Contest,
        Official International Personal Contest, Training Contest. Can be ``None``.
    icpc_region: :class:``str``
        Name of the Region for official ICPC Contests. Can be ``None``.
    country: :class:``str``
        The country from which the Contest was hosted. Can be ``None``.
    city: :class:``str``
        The city from which the Contest was hosted. Can be ``None``.
    season: :class:``str``
        The season of the Contest. Can be ``None``.
    """

    __slots__ = ["id", "name", "type", "phase", "frozen", "duration_seconds", "start_time_seconds",
                 "relative_time_seconds", "prepared_by", "website_url", "description", "difficulty", "kind",
                 "icpc_region", "country", "city", "season"]

    def __init__(self, dic):
        self.id: int = dic["id"]
        self.name: str = dic["name"]
        self.type: ContestType = ContestType[dic["type"]]
        self.phase: ContestPhase = ContestPhase[dic["phase"]]
        self.frozen: bool = dic["frozen"]
        self.duration_seconds: int = dic["durationSeconds"]
        self.start_time_seconds: int = dic.get("startTimeSeconds")  # Can be none
        self.relative_time_seconds: int = dic.get("relativeTimeSeconds")  # Can be none
        self.prepared_by: str = dic.get("preparedBy")  # Can be none
        self.website_url: str = dic.get("websiteUrl")  # Can be none
        self.description: str = dic.get("description")  # Can be none
        self.difficulty: int = dic.get("difficulty")  # Can be none. Integer from 1 to 5, larger = more difficult.
        self.kind: str = dic.get("kind")  # Can be none
        self.icpc_region: str = dic.get("icpcRegion")  # Can be none
        self.country: str = dic.get("country")  # Can be none
        self.city: str = dic.get("city")  # Can be none
        self.season: str = dic.get("season")  # Can be none

    def __eq__(self, other):
        return isinstance(other, Contest) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
