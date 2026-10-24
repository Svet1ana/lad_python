from rich.console import Console
from rich.table import Table

from blog import data

console = Console()

def create_post_menu() -> None:
    title = input("Enter title: ")
    author = input("Enter author: ")
    text = input("Enter text: ")
    data.create_post(title, author, text)
    console.print("Post created successfully")


def show_posts_menu() -> None:
    posts = data.list_posts()
    if not posts:
        console.print("[yellow]No posts found [/yellow]")
        return
    # for post in posts:
    #     print(f"{post['title']} by {post['author']} - {post['text']}")
    table = Table(title="Post list")
    table.add_column("Title")
    table.add_column("Author")
    table.add_column("Text")

    for post in posts:
        table.add_row(post["title"], post["author"], post["text"])
    console.print(table)


if __name__ == "__main__":
    print("Welcome to Blog")



