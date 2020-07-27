"""The Hack class for the CodeForces API."""

from dataclasses import dataclass

from api.return_objects.party import Party
from api.return_objects.problem import Problem


@dataclass
class JudgeProtocol:
    manual: bool
    protocol: str
    verdict: str


@dataclass
class Hack:
    """https://codeforces.com/apiHelp/objects#Hack"""

    id: int
    creation_time_seconds: int
    hacker: Party
    defender: Party
    verdict: int  # Can be none. Read docs for full enum documentation.
    problem: Problem
    test: str  # Can be none.
    judge_protocol: JudgeProtocol  # Can be none.

    def __eq__(self, other):
        return self.__eq__(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
