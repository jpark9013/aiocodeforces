"""The Submission class for the CodeForces API."""

from aiocodeforces.enum import SubmissionTestSet, SubmissionVerdict
from aiocodeforces.party import Party
from aiocodeforces.problem import Problem


class Submission:
    """
    Represents a submission on CodeForces.

    ..container:: operations

        ..describe:: x == y

            Checks if two Submissions are equal.

        ..describe: x != y

            Checks if two Submissions are not equal.

    Attributes
    -----------
    id: :class:``int``
        The ID of the Submission.
    contest_id: :class:``int``
        The contest ID of the Submission. Can be ``None``.
    creation_time_seconds: :class:``int``
        Time when Submission was created, in UNIX format.
    relative_time_seconds: :class:``int``
        Time after contest start when Submission was created.
    problem: :class:``Problem``
        The problem of the Submission.
    author: :class:``Party``
        The author of the Submission.
    programming_language: :class:``str``
        The programming language of the Submission.
    verdict: :class:``SubmissionVerdict``
        The verdict of the Submission. Can be ``None``.
    testset: :class:``SubmissionTestSet``
        Testset used for judging the Submission.
    passed_test_count: :class:``int``
        Number of passed tests.
    time_consumed_millis: :class:``int``
        Maximum time, in milliseconds, consumed by one test.
    memory_consumed_bytes: :class:``int``
        Maximum memory, in bytes, consumed by one test.
    points: :class:``float``
        Number of scored points for IOI-like contests. Can be ``None``.
    """

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
        self.verdict: SubmissionVerdict = SubmissionVerdict(dic.get("verdict")) if dic.get("verdict") else None
        self.testset: SubmissionTestSet = SubmissionTestSet(dic["testset"])
        self.passed_test_count: int = dic["passedTestCount"]
        self.time_consumed_millis: int = dic["timeConsumedMillis"]
        self.memory_consumed_bytes: int = dic["memoryConsumedBytes"]
        self.points: float = dic["points"]

    def __eq__(self, other):
        return isinstance(other, Submission) and self.id == other.id

    def __ne__(self, other):
        return self.__eq__(other)
