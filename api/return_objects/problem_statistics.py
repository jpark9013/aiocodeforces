"""The ProblemStatistics class for the CodeForces API."""

from dataclasses import dataclass


@dataclass
class ProblemStatistics:
    """https://codeforces.com/apiHelp/objects#ProblemStatistics"""

    contest_id: int  # Can be none
    index: str
    solved_count: int

    def __eq__(self, other):
        return isinstance(other, ProblemStatistics) and self.index == other.index

    def __ne__(self, other):
        return not self.__eq__(other)
