"""The ProblemStatistics class for the CodeForces API."""

from api.apirequestmaker import strip_dict


class ProblemStatistics:
    """
    Represents a Problem Statistic on CodeForces.

    ..container:: operations

        ..describe:: x == y

            Checks if two ProblemStatistics are equal.

        ..describe: x != y

            Checks if two ProblemStatistics are not equal.

    Attributes
    -----------
    contest_id: :class:``int``
        The ID of the contest for the ProblemStatistic. Can be ``None``.
    index: :class:``str``
        The index of the problem for the ProblemStatistic.
    solved_count: :class:``int``
        The number of users who solved the problem.
    """

    __slots__ = ["contest_id", "index", "solved_count"]

    def __init__(self, dic):
        dic = strip_dict(dic)
        self.contest_id: int = dic.get("contestId")  # Can be none
        self.index: str = dic["index"]
        self.solved_count: int = dic["solvedCount"]

    def __eq__(self, other):
        return isinstance(other, ProblemStatistics) and self.index == other.index

    def __ne__(self, other):
        return not self.__eq__(other)
