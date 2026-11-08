from l15_blog import Post, Author

def main() -> None:
    author = Author(name="Perelman", email="perelman@localhost")
    post1 = Post(title="Math", author=author, content="math 1")

    print("this is @property")
    print(post1.title)
    print("this is @author")
    print(post1.author)
    print(post1.title_length)


    post1.title = "new title"
    print(post1.title)

    try:
        post1.title = "    "
    except ValueError as e:
        print(e)






if __name__ == "__main__":
    main()