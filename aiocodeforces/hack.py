"""The Hack class for the CodeForces API."""

from aiocodeforces.party import Party
from aiocodeforces.problem import Problem


class JudgeProtocol:
    """Represents a JudgeProtocol on CodeForces.

    Attributes
    -----------
    manual: :class:``bool``
        Whether the Hack was manually entered.
    protocol: :class:``str``
        The protocol of the JudgeProtocol.
    verdict: :class:``str``
        The verdict of the JudgeProtocol.
    """

    __slots__ = ["manual", "protocol", "verdict"]

    def __init__(self, dic):
        self.manual: bool = dic["manual"]
        self.protocol: str = dic["protocol"]
        self.verdict: str = dic["verdict"]


class Hack:
    """Represents a Hack on CodeForces.

    ..container:: operations

        ..describe:: x == y

            Checks if two Hacks are equal.

        ..describe:: x != y

            Checks if two Hacks are not equal.

    Attributes
    -----------
    id: :class:``int``
        The ID of the Hack.
    creation_time_seconds: :class:``int``
        The Hack creation time, in UNIX.
    hacker: :class:``Party``
        The hacker.
    defender: :class:``Party``
        The defender.
    verdict: :class:``HackVerdict``
        The verdict of the Hack.
    problem: :class:``Problem``
        The problem that was hacked.
    test: :class:``str``
        The test of the Hack. Can be ``None``.
    judge_protocol: :class:``JudgeProtocol``
        The Judge Protocol of the Hack.
    """

    __slots__ = ["id", "creation_time_seconds", "hacker", "defender", "verdict", "problem", "test", "judge_protocol"]

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
