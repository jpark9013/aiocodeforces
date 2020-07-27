"""The ProblemStatistics class for the CodeForces API."""

from api.apirequestmaker import strip_dict


class ProblemStatistics:
    """https://codeforces.com/apiHelp/objects#ProblemStatistics"""

    def __init__(self, dic):
        strip_dict(dic)
        self.contest_id: int = dic.get("contestId")  # Can be none
        self.index: str = dic["index"]
        self.solved_count: int = dic["solvedCount"]

    def __eq__(self, other):
        return isinstance(other, ProblemStatistics) and self.index == other.index

    def __ne__(self, other):
        return not self.__eq__(other)
