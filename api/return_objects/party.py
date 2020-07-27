"""The Party class for the CodeForces API."""

from api.apirequestmaker import strip_dict
from api.return_objects.member import Member


class Party:
    """https://codeforces.com/apiHelp/objects#Party"""

    def __init__(self, dic):
        dic = strip_dict(dic)
        self.contest_id: int = dic["contestId"]
        self.members: list = [Member(i) for i in dic["members"]]  # of Members
        self.participant_type: int = dic["participantType"]  # Enum: CONTESTANT, PRACTICE, VIRTUAL, MANAGER,
        # OUT_OF_COMPETITION.
        self.team_id: int = dic.get("teamId")  # Can be none
        self.team_name: str = dic.get("teamName")  # Can be none
        self.ghost: bool = dic["ghost"]
        self.room: int = dic.get("room")  # Can be none
        self.start_time_seconds: int = dic.get("startTimeSeconds")  # Can be none

    def __eq__(self, other):
        return isinstance(other, Party) and self.contest_id == other.contest_id and self.members == other.members

    def __ne__(self, other):
        return not self.__eq__(other)
