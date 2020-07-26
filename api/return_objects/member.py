"""The Member class of the CodeForces API."""

from dataclasses import dataclass


@dataclass
class Member:
    """https://codeforces.com/apiHelp/objects#Member"""

    handle: str

    def __eq__(self, other):
        return isinstance(other, Member) and self.handle == other.handle

    def __ne__(self, other):
        return not self.__eq__(other)
