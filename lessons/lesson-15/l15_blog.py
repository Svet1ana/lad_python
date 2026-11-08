from datetime import datetime
from dataclasses import dataclass, field



class Author:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Author(name = {self.name!r},  email = {self.email!r})"

class Post:
    def __init__(self, title: str, content: str, author: Author, ):
        self.author = author
        self._title = title
        self.content = content

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Post title cannot be empty")
        self._title = value

    @property
    def title_length(self) -> int:
        return len(self._title)

    @property
    def slug(self) -> str:
        return self._title.lower().replace(" ", "-")


    def __str__(self) -> str:
            return f"Author: {self.author} , Title: {self._title}"

    def __repr__(self):
            return f"Post({self.author}, {self._title}, {self.content})"


@dataclass
class Comment:
    text: str
    author: str
    likes: int = 0
    tags: list[str] = field(default_factory=list)
    date: datetime = field(default_factory=datetime.now)


    def __str__(self) -> str:
        return f"Comment from: {self.author}, date: {self.date}"


class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.posts: list[Post] = []

    def add(self, post: Post) -> None:
        self.posts.append(post)

    def __len__(self) -> int:
        return len(self.posts)

    def __contains__(self, post: Post) -> bool:
        return post in self.posts

    def __getitem__(self, index: int) -> Post:
        return self.posts[index]

    def __str__(self) -> str:
        return f"Category: ({self.name})"

    def __repr__(self) -> str:
        return f"Category(name = {self.name!r}, posts = {self.posts})"