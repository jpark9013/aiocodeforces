"""The Party class for the CodeForces API."""

from aiocodeforces.enum import PartyParticipantType
from aiocodeforces.member import Member


class Party:
    """Represents a Party on CodeForces.

    ..container:: operations

        ..describe:: x == y

            Checks if two Parties are equal.

        ..describe: x != y

            Checks if two Parties are not equal.

    Attributes
    -----------
    contest_id: :class:``int``
        The Contest ID of the Contest in which the Party is participating in.
    members: :class:``list``
        The list of members within the Party.
    participant_type: :class:``PartyParticipantType``
        The participant type of the Party.
    team_id: :class:``int``
        The ID of the Party. Can be ``None``.
    team_name: :class:``str``
        The name of the Party. Can be ``None``.
    ghost: :class:``bool``
        Whether the Party is a ghost in the Contest or not (if their rating is impacted).
    room: :class:``int``
        The room of the Party. Can be ``None``.
    start_time_seconds: :class:``int``
        The start time when the Party started the Contest. Can be ``None``.
    """

    __slots__ = ["contest_id", "members", "participant_type", "team_id", "team_name", "ghost", "room",
                 "start_time_seconds"]

    def __init__(self, dic):
        self.contest_id: int = dic["contestId"]
        self.members: list = [Member(i) for i in dic["members"]]  # of Members
        self.participant_type: PartyParticipantType = PartyParticipantType(dic["participantType"])
        self.team_id: int = dic.get("teamId")  # Can be none
        self.team_name: str = dic.get("teamName")  # Can be none
        self.ghost: bool = dic["ghost"]
        self.room: int = dic.get("room")  # Can be none
        self.start_time_seconds: int = dic.get("startTimeSeconds")  # Can be none

    def __eq__(self, other):
        return isinstance(other, Party) and self.contest_id == other.contest_id and self.members == other.members

    def __ne__(self, other):
        return not self.__eq__(other)
