from l3_task4 import title

articles = []

def create_article(title: str, author: str, category: str, rating: float)-> dict:
    """Создается словарь статьи и добавляет его в списко"""
    article = {
        "title": title,
        "author": author,
        "category": category,
        "rating": rating
    }
    articles.append(article)
    return article


def show_articles(articles_list: list) -> None:
    """ВЫводит все статьи"""
    if not articles_list:
        print("Списко статей пуст")
        return

    for num, article in enumerate(articles_list, start=1):
        print(f"{num}. {article['title']}, Автор - {article['author']}, "
              f"Категория - {article['category']}, ")

def filter_by_category(articles_list: list, category: str) -> list:
    """Возвращает статьи выбранной категории"""
    return [article for article in articles_list if article['category'] == category]

def sort_articles(articles_list: list, key: str = "rating", reverse: bool   = False) -> list:
    """Возвращает отсортированный список"""
    return sorted(articles_list, key=lambda x: x.get(key,"rating"), reverse=reverse)

def show_help() -> None:
    """показывает списко достыпных команд"""
    print("""
            Доступные команды: 
            add - доавить статью
            show - показать все статьи 
            filter - отфильтровать по категории
            sort -  отсортировать статьи по выбраному значению
            help - показать справку
            quit - выйти
        """)

print("мини проект блог CLI")
show_help()

while True:
    command = input("Введите команду    ").strip().lower()

    if command == "add":
        title = input("Заголоовк:")
        author = input("Автор:")
        category = input("Категория:")
        rating = float(input("Рейтинг:"))

        create_article(title, author, category, rating)
        print("Статья добавлена")

    elif command == "show":
        show_articles(articles)

    elif command == "filter":
        category = input("категоиря:")
        filtered_articles = filter_by_category(articles, category)
        print(f"В категории {category} {len(filtered_articles)} статей")
        show_articles(filtered_articles)

    elif command == "sort":
        key = input("Поле для сортировки (title, author, category, rating):")
        reverse = input("Сортировать по убыванию? ")

        if reverse:
            reverse = True
        else:
            reverse = False

        sorted_articlse = sort_articles(sort_articles)

    elif command == "help":
        show_help()

    elif command == "quit":
        print("Выход из программы")

    else:
        print("Команда неизвестаня введите help")