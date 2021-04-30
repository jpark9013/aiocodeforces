class BlogEntry:

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
