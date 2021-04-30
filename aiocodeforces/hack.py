from aiocodeforces.enum import SubmissionVerdict
from aiocodeforces.party import Party
from aiocodeforces.problem import Problem


class JudgeProtocol:

    __slots__ = ["manual", "protocol", "verdict"]

    def __init__(self, dic):
        self.manual: bool = dic["manual"]
        self.protocol: str = dic["protocol"]
        self.verdict: str = dic["verdict"]


class Hack:

    __slots__ = ["id", "creation_time_seconds", "hacker", "defender", "verdict", "problem", "test", "judge_protocol"]

    def __init__(self, dic):
        self.id: int = dic["id"]
        self.creation_time_seconds: int = dic["creationTimeSeconds"]
        self.hacker: Party = Party(dic["hacker"])
        self.defender: Party = Party(dic["defender"])
        self.verdict: SubmissionVerdict = SubmissionVerdict(dic.get("verdict")) if dic.get("verdict") else None
        self.problem: Problem = Problem(dic["problem"])
        self.test: str = dic.get("test")  # Can be none.
        self.judge_protocol: JudgeProtocol = JudgeProtocol(dic.get("judgeProtocol")) if dic.get("judgeProtocol") \
            else None  # Can be none.

    def __eq__(self, other):
        return self.__eq__(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
