

class Post:
    def __init__(self, title:str, text:str, author:str) -> None:
        self.title = title
        self.body = text
        self.author = text
        self.likes = 0



first = Post(title="Занимательный Питон", text="Первый текст", author="Россо")
second = Post(title="Занимательный физика", text="второй текст", author="Перельман")


print(first.title)
print(second.title)
print(first.likes)


print(second is first.likes)
print(type(first))
print(type(second))