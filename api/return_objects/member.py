"""The Member class of the CodeForces API."""

from api.apirequestmaker import strip_dict


class Member:
    """Represents a Member on CodeForces.

    ..container:: operations

        ..describe:: x == y

            Checks if two Members are equal.

        ..describe:: x != y

            Checks if two Members are not equal.

    Attributes
    -----------
    handle: :class:``str``
        The handle of the Member.
    """

    __slots__ = ["handle"]

    def __init__(self, dic):
        dic = strip_dict(dic)
        self.handle: str = dic["handle"]

    def __eq__(self, other):
        return isinstance(other, Member) and self.handle == other.handle

    def __ne__(self, other):
        return not self.__eq__(other)
