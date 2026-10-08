from random import choice

posts = [
    ["2026-02-10", "Как установить uv", "Инструментарий"],
    ["2026-02-14", "Списки в Python", "Python"],
    ["2026-02-18", "Введение в Django", "Django"],
]

print(posts)

while True:
    print(
        """
        Что делаем? 
        1 - Добавить пост
        2 - Показать все посты
        3 - отсортировать по дате
        4 - отфильтровать по категории
        0 - выйти
        """
    )
    choice = input("Ваш выбор: ")

    if choice == "1":
        new_date = input("введите дату в формате ГГГГ-ММ-ДД (пример 2026-02-18): ")
        new_title = input("введите заголовок: ")
        new_category = input("введите категорию: ")

        posts.append([new_date, new_title, new_category])
        print(f"Пост добвален {posts[-1]}")
        print(f"Пост \"{new_title}\" добвален ")


    elif choice == "2":
        print("\n все посты: ")
        for post in posts:
            print(f"Дата {post[0]} - {post[1]} - {post[2]} ")

    elif choice == "3":
        posts.sort()
        print("\n отсортировано по дате: ")
        for post in posts:
            print(f" {post[0]} - {post[1]} - {post[2]} ")
            
    elif choice == "4":
        target = input("введите категорию по которой будем фильтровать: ")
        filtered = [post for post in posts if post[2] == target  ]
        print(f"\nПосты в категории: {target}:")
        if filtered:
            for post in filtered:
                print(f" {post[0]} - {post[1]} - {post[2]} ")
        else:
            print("Статей нет")

    elif choice == "0":
        print("До свидания")
        break

    else:
        print("Попробуй еще раз!")