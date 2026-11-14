from datetime import datetime


class Author:
    def __init__(self, id: int, name: str) -> None:
        self.name = name
        self.id = id
        self._posts: list["Post"] = []

    def add_post(self, post: "Post") -> None:
        post.author = self
        if post not in self._posts:
            self._posts.append(post)


    @property
    def post(self) -> list["Post"]:
        return self._posts.copy()

    def post_count(self) -> int:
        return len(self._posts)

    def __str__(self) -> str:
        return f"[{self.name}, {self.id}]"

    def __repr__(self) -> str:
        return f"Author(id={self.id}, name={self.name!r})"


class Category:
    def __init__(self, id: int, title: str) -> None:
        self.id = id
        self.title = title

        self._post: list["Post"] = []

    def add_post(self, post: list["Post"]) -> None:
        post.category = self
        if post not in self._posts:
            self._posts.append(post)

    @property
    def post(self) -> list["Post"]:
        return self._posts.copy()

    def post_count(self) -> int:
        return len(self._posts)

    def __str__(self) -> str:
        return f"Category number [{self.title}, {self.id}]"

    def __repr__(self) -> str:
        return f"Category(id={self.id}, title={self.title!r})"


class Tag:
    def __init__(self, id: int, title: str) -> None:
        self.id = id
        self.title = title
        self._posts: list["Post"] = []


    def add_post(self, post: list["Post"]) -> None:
        if post not in self._posts:
            self._posts.append(post)

    @property
    def post(self) -> list["Post"]:
        return self._posts.copy()

    def __str__(self) -> str:
        return f"Tag number [{self.title}, {self.id}]"

    def __repr__(self) -> str:
        return f"Tag(id={self.id}, title={self.title!r})"


class Post:
    def __init__(self, id: int, title: str, content: str, author: Author , category: Category) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.category = category

        self.tags: list["Tag"] = []
        self.created_add = datetime.now()

    def add_tag(self, tag: Tag) -> None:
        if tag not in self.tags:
            self.tags.append(tag)
            tag.add_post(self)

    @property
    def tag_title(self) -> list[str]:
        return [tag.title for tag in self.tags]

    def __str__(self) -> str:
        return f"Post number [{self.id}, {self.title}]"

    def __repr__(self) -> str:
        return f"Post(id={self.id}, title={self.title!r}, content={self.content!r}, author={self.author}, category={self.category})"


