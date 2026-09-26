posts = [
    "Пульсирующая вселенная",
    "Занимательная строномия",
    "Кортежи в Питоне",
]
print("Свеие статьи: ")

for number, title in enumerate(posts, start=1):
    print(f"{number}. {title}")

print("\nкарточка статьи ")
for title in posts:
    print(f"{title} - {len(title)} символов")

print("\nПоиск ")
if "Пульсирующая"  in posts:
    print("Пост есть в списке")
else:
    print("Такой статьи нет")