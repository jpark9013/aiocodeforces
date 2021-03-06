from aiocodeforces.enum import ContestPhase, ContestType


class Contest:

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
