"""The Hack class for the CodeForces API."""

from api.return_objects.party import Party
from api.return_objects.problem import Problem


class JudgeProtocol:
    def __init__(self, dic):
        self.manual: bool = dic["manual"]
        self.protocol: str = dic["protocol"]
        self.verdict: str = dic["verdict"]


class Hack:
    """https://codeforces.com/apiHelp/objects#Hack"""

    def __init__(self, dic):
        self.id: int = dic["id"]
        self.creation_time_seconds: int = dic["creationTimeSeconds"]
        self.hacker: Party = Party(dic["hacker"])
        self.defender: Party = Party(dic["defender"])
        self.verdict: int = dic.get("verdict")  # Can be none. Read docs for full enum documentation.
        self.problem: Problem = Problem(dic["problem"])
        self.test: str = dic.get("test")  # Can be none.
        self.judge_protocol: JudgeProtocol = JudgeProtocol(dic.get("judgeProtocol")) if dic.get("judgeProtocol") \
            else None  # Can be none.

    def __eq__(self, other):
        return self.__eq__(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
