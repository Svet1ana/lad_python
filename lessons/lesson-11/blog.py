import json
from pathlib import Path

DATA_FILE = Path("articles.json")


def load_articles() -> list:
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_articles(articles: list) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(articles, file, ensure_ascii=False, indent=4)


def main() -> None:
    articles = load_articles()
    title = input("Enter a title: ")
    author = input("Enter a author: ")
    new_post = {"title": title, "author": author}
    articles.append(new_post)
    save_articles(articles)
    print("article saved")

    # print(f"current list of articles:")
    # for num, article in enumerate(articles, start=1):
    #     print(f"{num}. {article['title']}")

    # Внимательно поигарться с этимии двумя варинатами печати
    print("current list of articles:")
    for article in enumerate(articles, start=1):
        print(f" {article[0]} . {article[1]['title']} - {article[1]['author']}")


if __name__ == "__main__":
    main()