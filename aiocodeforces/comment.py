"""The Comment class for the CodeForces API."""


class Comment:
    """Represents a CodeForces comment.

    ..container:: operations

        ..describe:: x == y

            Checks if two Comments are equal.

        ..describe:: x != y

            Checks if two Comments are not equal.

    Attributes
    -----------
    id: :class:``int``
        The ID of the comment.
    creation_time_seconds: :class:``int``
        The creation time of the comment in seconds.
    commentator_handle: :class:``str``
        The handle of the comment author.
    locale: :class:``str``
        The locale of the comment.
    text: :class:``str``
        The content of the comment.
    parent_comment_id: Optional[:class:``int``]
        The parent comment's ID. ``None`` if it doesn't exist.
    rating: Optional[:class:``int``]
        The rating of the comment. ``None`` if it doesn't exist.
    """

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
