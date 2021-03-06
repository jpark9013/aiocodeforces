class Member:

    __slots__ = ["handle"]

    def __init__(self, dic):
        self.handle: str = dic["handle"]

    def __eq__(self, other):
        return isinstance(other, Member) and self.handle == other.handle

    def __ne__(self, other):
        return not self.__eq__(other)
