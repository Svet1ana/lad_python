class Post:
    platform = "blog CLI"
    def __init__(self, title:str, text:str, author:str) -> None:
        self.title = title
        self.body = text
        self.author = text
        self.likes = 0

    def display(self) -> None:
        print(f"Название статьи: {self.title}, автор {self.author}, количество лайков : {self.likes}"  )

    def add_like(self) -> None:
        self.likes += 1


first = Post(title="Занимательный Питон", text="Первый текст", author="Россо")
second = Post(title="Занимательный физика", text="второй текст", author="Перельман")

first.add_like()
first.add_like()

second.add_like()

first.display()
second.display()

print(first.platform)
print(second.platform)
print(Post.platform)

Post.display(first)