"""The BlogEntry class for the CodeForces API"""


class BlogEntry:
    """Represents a CodeForces Blog Entry.

    .. container:: operations

        .. describe:: x == y

            Checks if two BlogEntries are equal.

        .. describe:: x != y

            Checks if two BlogEntries are not equal.

    Attributes
    -----------
    id: :class:``int``
        The BlogEntry's id.
    original_locale: :class:``str``
        The BlogEntry's original locale.
    creation_time_seconds: :class:``int``
        The BlogEntry's original creation time in seconds.
    author_handle: :class:``str``
        The BlogEntry's author handle.
    title: :class:``str``
        The BlogEntry's title.
    locale: :class:``str``
        The BlogEntry's current locale.
    modification_time_seconds: :class:``int``
        The BlogEntry's last time updated.
    allow_view_history: :class:``bool``
        Whether or not the BlogEntry allows you to view its revision history.
    tags: :class:``list``
        A :class:``list`` of :class:``str`` which represent the tags.
    """

    __slots__ = ["id", "original_locale", "creation_time_seconds", "author_handle", "title", "locale",
                 "modification_time_seconds", "allow_view_history", "tags", "rating", "content"]

    def __init__(self, dic):
        self.id: int = dic["id"]
        self.original_locale: str = dic["originalLocale"]
        self.creation_time_seconds: int = dic["creationTimeSeconds"]
        self.author_handle: str = dic["authorHandle"]
        self.title: str = dic["title"]
        self.locale: str = dic["locale"]
        self.modification_time_seconds: int = dic["modificationTimeSeconds"]
        self.allow_view_history: bool = dic["allowViewHistory"]
        self.tags: list = dic["tags"]  # Of strings
        self.rating: int = dic["rating"]
        self.content: str = dic.get("content")

    def __eq__(self, other):
        return isinstance(other, BlogEntry) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
