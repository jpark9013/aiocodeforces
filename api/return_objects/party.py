"""The Party class for the CodeForces API."""

from dataclasses import dataclass


@dataclass
class Party:
    """https://codeforces.com/apiHelp/objects#Party"""

    contest_id: int
    members: list  # of Members
    participant_type: int  # Enum: CONTESTANT, PRACTICE, VIRTUAL, MANAGER, OUT_OF_COMPETITION.
    team_id: int  # Can be none
    team_name: str  # Can be none
    ghost: bool
    room: int  # Can be none
    start_time_seconds: int  # Can be none

    def __eq__(self, other):
        return isinstance(other, Party) and self.contest_id == other.contest_id and self.members == other.members

    def __ne__(self, other):
        return not self.__eq__(other)
