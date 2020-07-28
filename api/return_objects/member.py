"""The Member class of the CodeForces API."""

from api.apirequestmaker import strip_dict


class Member:
    """https://codeforces.com/apiHelp/objects#Member"""

    __slots__ = ["handle"]

    def __init__(self, dic):
        dic = strip_dict(dic)
        self.handle: str = dic["handle"]

    def __eq__(self, other):
        return isinstance(other, Member) and self.handle == other.handle

    def __ne__(self, other):
        return not self.__eq__(other)
