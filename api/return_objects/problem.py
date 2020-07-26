"""The Problem class for the CodeForces API."""

from dataclasses import dataclass


@dataclass
class Problem:
    """https://codeforces.com/apiHelp/objects#Problem"""

    contest_id: int  # Can be none
    problemset_name: str  # Can be none
    index: str
    name: str
    type: int  # Enum: PROGRAMMING, QUESTION
    points: float
    rating: int  # Can be none
    tags: list  # Of strings.

    def __eq__(self, other):
        return isinstance(other, Problem) and self.index == other.index

    def __ne__(self, other):
        return not self.__eq__(other)
