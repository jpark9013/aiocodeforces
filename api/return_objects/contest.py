"""The Contest class for the CodeForces API."""

from dataclasses import dataclass


@dataclass
class Contest:
    """https://codeforces.com/apiHelp/objects#Contest"""

    id: int
    name: str
    type: int  # Enum: CF, IOI, ICPC. Scoring system used for the contest.
    phase: int  # Enum: BEFORE, CODING, PENDING_SYSTEM_TEST, SYSTEM_TEST, FINISHED.
    frozen: bool
    duration_seconds: int
    start_time_seconds: int  # Can be none
    relative_time_seconds: int  # Can be none
    prepared_by: str  # Can be none
    website_url: str  # Can be none
    description: str  # Can be none
    difficulty: int  # Can be none. Integer from 1 to 5, larger = more difficult.
    kind: str  # Can be none
    icpc_region: str  # Can be none
    country: str  # Can be none
    city: str  # Can be none
    season: str  # Can be none

    def __eq__(self, other):
        return isinstance(other, Contest) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
