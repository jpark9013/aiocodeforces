"""The Contest class for the CodeForces API."""

from api.apirequestmaker import strip_dict


class Contest:
    """https://codeforces.com/apiHelp/objects#Contest"""

    def __init__(self, dic):
        strip_dict(dic)
        self.id: int = dic["id"]
        self.name: str = dic["name"]
        self.type: int = dic["type"]  # Enum: CF, IOI, ICPC. Scoring system used for the contest.
        self.phase: int = dic["phase"]  # Enum: BEFORE, CODING, PENDING_SYSTEM_TEST, SYSTEM_TEST, FINISHED.
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
