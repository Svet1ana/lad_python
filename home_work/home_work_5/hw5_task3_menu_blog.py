"""
Меню блога (список постов).
Заведите список постов — каждый пост это список [дата, заголовок, категория] (дата в формате ГГГГ-ММ-ДД).
Выведите все посты, отсортируйте их по дате, а затем отфильтруйте по введённой с клавиатуры категории.
Если в этой категории постов нет — выведите сообщение об этом.
"""

posts = [
    ["2026-11-07", "Strings in Python", "Python"],
    ["2026-11-01", "The First Test", "QA"],
    ["2026-11-03", "While", "Python"],
    ["2026-11-05", "BD", "SQL"],
]


def print_posts(items):
    for date, title, category in items:
        print(f"{date} | {title} | {category}")


print("All posts:")
print_posts(posts)

by_date = sorted(posts, key=lambda post: post[0])

print("\nBy date, from old to new:")
print_posts(by_date)

requested = input("\nEnter category: ").strip().lower()
found = [post for post in by_date if post[2].lower() == requested]

if found:
    print_posts(found)
else:
    print("There are no posts in this category.")