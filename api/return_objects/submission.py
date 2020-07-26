"""The Submission class for the CodeForces API."""

from dataclasses import dataclass

from api.return_objects.party import Party
from api.return_objects.problem import Problem


@dataclass
class Submission:
    """https://codeforces.com/apiHelp/objects#Submission"""

    id: int
    contest_id: int
    creation_time_seconds: int
    relative_time_seconds: int
    problem: Problem
    author: Party
    programming_language: str
    verdict: int  # Can be none, read CF API docs for full enum
    testset: int  # Enum: SAMPLES, PRETESTS, TESTS, CHALLENGES, TESTS1, ..., TESTS10.
    passed_test_count: int
    time_consumed_millis: int
    memory_consumed_bytes: int
    points: float

    def __eq__(self, other):
        return isinstance(other, Submission) and self.id == other.id

    def __ne__(self, other):
        return self.__eq__(other)
