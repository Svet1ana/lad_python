from blog_app.managers import Blog
from blog_app.models import Author, Category, Tag, Post


def find_category(blog: Blog, title: str) -> Category | None:
    for category in blog._categories:
        if category.title == title:
            return category
        return None

def find_author(blog: Blog, name: str) -> Author | None:
    for author in blog._authors:
        if author.name == name:
            return author
    return None

def main() -> None:
    blog = Blog()

    Peter = blog.add_author(name='Peter')
    Sam = blog.add_author(name='Sam')

    backed = blog.add_category(title='Backed')
    frontend = blog.add_category(title='Frontend')

    python = blog.add_tag(title='Python')
    java = blog.add_tag(title='Java')
    django = blog.add_tag(title='Django')


    post1 = blog.create_post(title="New Python")
    post2 = blog.create_post(title="New Java")

