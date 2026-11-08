from l15_blog import Post, Author, Category, Comment

def main() -> None:
    
    author = Author(name="Gvido" , email="gvido.com")
    news_category = Category(name="News Python")
    it_category = Category(name="IT")

    news_category.add(Post(title="News Python",author=author, content="IT Python"))
    news_category.add(Post(title="News Java", author=author, content="IT JAVA"))
    it_category.add(Post(title="News Java", author=author, content="IT JAVA"))

    print("Posts of Category News:")
    for post in news_category:
        print(post)


    print("Posts of Category IT: {len(news_category)}")

    it_post = it_category [0]
    print(it_post.title)
    print(f"This post is in category IT: {it_post in it_category}")

    for post in news_category:
        print(f"Title: {post.title}, Lenth : {post.title_length}, Taags : {post.slug}")



if __name__ == "__main__":
    main()