import json
import keyword
from dataclasses import dataclass
from json import JSONDecodeError
from pathlib import Path


DB_PATH = Path("Blog.json")

@dataclass
class Post:
    title: str
    author: str
    category: str
    views: int


    def as_dict(self) -> dict[str, object]:
        return {"title": self.title, "author": self.author, "category": self.category, "views": self.views}

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Post":
        return cls(
            title=str(data["title"]),
             author=str(data["author"]),
             category=str(data["category"]),
             views=int(data["views"]))

    def __str__(self) -> str:
        return f"Post({self.title}, {self.author}, {self.category}, {self.views})"


class BlogRepository:
    def __init__(self, path = DB_PATH) -> None:
        self.path = path

    def load(self) -> list[Post]:
        if not self.path.exists():
            return []

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                raw = json.load(f)
        except JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}") from e

        return [Post.from_dict(post) for post in raw]

    def save(self, posts: list[Post]) -> None:
        data = [post.as_dict() for post in posts]
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


def add_post(posts: list[Post]) -> None:
    title = input("Enter title: ")
    author = input("Enter author: ")
    category = input("Enter category: ")

    if not title or not author or not category:
        raise ValueError("Invalid input")

    posts.append(Post(title=title, author=author, category=category, views=0))
    print(f"Added {len(posts)} posts")

def list_posts(posts: list[Post] ) -> None:
    if not posts:
        print("No posts")
        return

    for num, post in enumerate(posts, start=1):
        print(f"{num}. {post.title}. {post.category}. {post.views}")

def search_posts(posts: list[Post], keyword: str) -> list[Post]:
    keywords = keyword.lower().strip()

    return [post for post in posts if keywords in post.title.lower()]

def main() -> None:
    repo = BlogRepository()

    try:
        posts = repo.load()
    except ValueError as e:
        print(f"load error: {e}")
        posts = []

    print(" MENU: 1 - Add posts, 2 - List posts, 3 - Search posts, 4 - Exit")

    while True:
        command = input("> ").strip().lower()

        match command:
            case "1"| "add":
                try:
                    add_post(posts)
                except ValueError as e:
                    print(f"add error: {e}")
            case "2" | "list":
                list_posts(posts)
            case "3" | "search":
                keyword = input("Enter keyword: ")
                if search_resul := search_posts(posts, keyword):
                    list_posts(search_resul)
                else:
                    print("Invalid input")
            case "4" | "exit":
                try:
                    repo.save(posts)
                    print("all were saved")
                except OSError as e:
                    print(f"save error: {e}")
                break
            case _:
                print("Invalid input")



if __name__ == "__main__":
    main()


