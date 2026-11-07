titles = [
    "Python для начинающих",
    "Как устроен HTTP",
    "Строки в Python",
]

print("Заголовки с Python:")
for title in titles:
    if "Python" in title:
        print(title)

print("Slug каждого заголовка:")
for title in titles:
    print(title, "→", build_slug(title))