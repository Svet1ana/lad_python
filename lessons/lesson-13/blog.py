class Author:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        
        
class Category():
    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        return self.title


class Post:
    def __init__(self, title: str, text: str, author: Author, category: Category):
        self.title = title
        self.text = text
        self.author = author
        self.category = category
        
    def display(self):
        print(f"Категоиря {self.category} , Название {self.title} , Автор {self.author.name} ")
       
       
posts = []

def add_post() -> None:
    author_name = input("введите имя автора: ")
    author_email = input("введите email автора: ")
    category = input("введите категорию: ")
    title = input("введите название: ")
    text = input("введите текст: ")

    new_author = Author(author_name, author_email)
    new_category = Category(category)
    new_post = Post(title, text, new_author, new_category)

    posts.append(new_post)
    print("Пост добавлне \n")


def show_posts() -> None:
    if not posts:
        print("Нет записей")
        return
    for post in posts:
        post.display()

while True:
    action = input("Выберетие действия: add, show, exit ").lower().strip()
    if action == "add":
        add_post()
    elif action == "show":
        show_posts()
    elif action == "exit":
        break
    else:
        print("неизветсаня команда")


