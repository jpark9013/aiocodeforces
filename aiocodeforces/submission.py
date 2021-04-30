from aiocodeforces.enum import SubmissionTestSet, SubmissionVerdict
from aiocodeforces.party import Party
from aiocodeforces.problem import Problem


class Submission:

    __slots__ = ["id", "contest_id", "creation_time_seconds", "relative_time_seconds", "problem", "author",
                 "programming_language", "verdict", "testset", "passed_test_count", "time_consumed_millis",
                 "memory_consumed_bytes", "points"]

    def __init__(self, dic):
        self.id: int = dic["id"]
        self.contest_id: int = dic["contestId"]
        self.creation_time_seconds: int = dic["creationTimeSeconds"]
        self.relative_time_seconds: int = dic["relativeTimeSeconds"]
        self.problem: Problem = Problem(dic["problem"])
        self.author: Party = Party(dic["author"])
        self.programming_language: str = dic["programmingLanguage"]
        self.verdict: SubmissionVerdict = SubmissionVerdict[dic.get("verdict")] if dic.get("verdict") else None
        self.testset: SubmissionTestSet = SubmissionTestSet[dic["testset"]]
        self.passed_test_count: int = dic["passedTestCount"]
        self.time_consumed_millis: int = dic["timeConsumedMillis"]
        self.memory_consumed_bytes: int = dic["memoryConsumedBytes"]
        self.points: float = dic["points"]

    def __eq__(self, other):
        return isinstance(other, Submission) and self.id == other.id

    def __ne__(self, other):
        return self.__eq__(other)
