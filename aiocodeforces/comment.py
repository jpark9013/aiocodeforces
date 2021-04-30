class Comment:

    __slots__ = ["id", "creation_time_seconds", "commentator_handle", "locale", "text", "parent_comment_id", "rating"]

    def __init__(self, dic):
        self.id: int = dic["id"]
        self.creation_time_seconds: int = dic["creationTimeSeconds"]
        self.commentator_handle: str = dic["commentatorHandle"]
        self.locale: str = dic["locale"]
        self.text: str = dic["text"]
        self.parent_comment_id: int = dic.get("parentCommentId")  # Can be none
        self.rating: int = dic.get("rating")

    def __eq__(self, other):
        return isinstance(other, Comment) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
