"""The Submission class for the CodeForces API."""

from dataclasses import dataclass

from api.return_objects.party import Party
from api.return_objects.problem import Problem


@dataclass
class Submission:
    """https://codeforces.com/apiHelp/objects#Submission"""

    def __init__(self, dic):
        self.id: int = dic["id"]
        self.contest_id: int = dic["contestId"]
        self.creation_time_seconds: int = dic["creationTimeSeconds"]
        self.relative_time_seconds: int = dic["relativeTimeSeconds"]
        self.problem: Problem = Problem(dic["problem"])
        self.author: Party = Party(dic["author"])
        self.programming_language: str = dic["programmingLanguage"]
        self.verdict: int = dic.get("verdict")  # Can be none, read CF API docs for full enum
        self.testset: int = dic["testset"]  # Enum: SAMPLES, PRETESTS, TESTS, CHALLENGES, TESTS1, ..., TESTS10.
        self.passed_test_count: int = dic["passedTestCount"]
        self.time_consumed_millis: int = dic["timeConsumedMillis"]
        self.memory_consumed_bytes: int = dic["memoryConsumedBytes"]
        self.points: float = dic["points"]

    def __eq__(self, other):
        return isinstance(other, Submission) and self.id == other.id

    def __ne__(self, other):
        return self.__eq__(other)
