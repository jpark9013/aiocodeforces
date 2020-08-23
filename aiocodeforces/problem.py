"""The Problem class for the CodeForces API."""

from aiocodeforces.enum import ProblemType


class Problem:
    """
    ..container:: operations

        ..describe:: x == y

            Checks if two Problems are equal.

        ..describe:: x != y

            Checks if two Problems are not equal.

    Attributes
    -----------
    contest_id: :class:``int``
        The ID of the contest containing the problem. Can be ``None``.
    problemset_name: :class:``str``
        The name of the set containing the problem. Can be ``None``.
    index: :class:``str``
        The index of the Problem.
    name: :class:``str``
        The name of the Problem.
    type: :class:``ProblemType``
        The type of the Problem.
    points: :class:``float``
        Maximum amount of points for the problem.
    rating: :class:``int``
        Problem rating. Can be ``None``.
    tags: :class:``list``
        A list of strings containing the tags.
    """

    __slots__ = ["contest_id", "problemset_name", "index", "name", "type", "points", "rating", "tags"]

    def __init__(self, dic):
        self.contest_id: int = dic.get("contestId")  # Can be none
        self.problemset_name: str = dic.get("problemsetName")  # Can be none
        self.index: str = dic["index"]
        self.name: str = dic["name"]
        self.type: ProblemType = ProblemType(dic["type"])  # Enum: PROGRAMMING, QUESTION
        self.points: float = dic["points"]
        self.rating: int = dic["rating"]  # Can be none
        self.tags: list = dic["tags"]  # Of strings.

    def __eq__(self, other):
        return isinstance(other, Problem) and self.index == other.index

    def __ne__(self, other):
        return not self.__eq__(other)
