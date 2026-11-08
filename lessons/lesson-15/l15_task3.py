from l15_blog import Comment

def main() -> None:
    comment1  = Comment(author="Perelman", text="New test text", likes=1)
    comment2  = Comment(author="Perelman", text="New test text", likes=1)
    comment3  = Comment(author="Perelman", text="New test text", tags=["Python", "Django"])
    comment4 = comment1
    # comment5 = eval(repr(comment1))


    print(comment1)
    print(comment2 == comment1)
    print(comment2 is comment1)
    print(comment4 is comment1)
    # print(comment5 is comment1)

    comment1.tags.append("JS")
    print(comment1.tags)
    print(comment2.tags)
    print(comment3.tags)


if __name__ == "__main__":
    main()