from l15_blog import Post, Author


def main() -> None:
    author = Author(name="Perelman", email="perelman@localhost")
    post1 = Post(title="Math", author=author, content="math 1")
    post2 = Post(title="Math PRO", author=author, content="math 2")

    print(" This is  __str__")
    print(post1)
    print(author)

    print(" This is  __repr__")
    print(repr(post2))
    print(repr(author))

    print(f"{author} - {author=}_")

    print("List o f posts: ")
    posts = [post1, post2]
    print(posts)


if __name__ == "__main__":
    main()