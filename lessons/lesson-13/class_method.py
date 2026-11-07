from typing import Self


class Post:
    def __init__(self, title:str, text:str, author:str) -> None:
        self.title = title
        self.body = text
        self.author = text
        self.likes = 0

    def display(self) -> None:
        print(f"Название статьи: {self.title}, автор {self.author}" )

    @staticmethod
    def is_valid_title(title:str) -> bool:
        return isinstance(title, str) and bool(title.strip())

    @classmethod
    # def from_csv(cls, row: str) -> Self:
    def from_csv(cls, row: str) -> "Post":
        title, author, text = row.split(";")
        if not cls.is_valid_title(title): #False первращаем мв True
            raise ValueError("Invalid title")
        return cls(title, author, text )

post = Post.from_csv("Занимательная математика; Перельман; Мой первый пост")
post.display()

print(Post.is_valid_title("Занимательная химия"))
print(Post.is_valid_title(1))
print(Post.is_valid_title(post.title))


title = input("Введите заголвоок статьи")
author = "Vasyf"
text = "TEXT"

if Post.is_valid_title(title):
    new_post = Post(title, text, author)
    new_post.display()
