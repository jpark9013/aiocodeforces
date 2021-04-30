from aiocodeforces.enum import ProblemType


class Problem:

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
