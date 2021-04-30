from aiocodeforces.enum import PartyParticipantType
from aiocodeforces.member import Member


class Party:

    __slots__ = ["contest_id", "members", "participant_type", "team_id", "team_name", "ghost", "room",
                 "start_time_seconds"]

    def __init__(self, dic):
        self.contest_id: int = dic["contestId"]
        self.members: list = [Member(i) for i in dic["members"]]  # of Members
        self.participant_type: PartyParticipantType = PartyParticipantType[dic["participantType"]]
        self.team_id: int = dic.get("teamId")  # Can be none
        self.team_name: str = dic.get("teamName")  # Can be none
        self.ghost: bool = dic["ghost"]
        self.room: int = dic.get("room")  # Can be none
        self.start_time_seconds: int = dic.get("startTimeSeconds")  # Can be none

    def __eq__(self, other):
        return isinstance(other, Party) and self.contest_id == other.contest_id and self.members == other.members

    def __ne__(self, other):
        return not self.__eq__(other)
