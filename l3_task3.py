from main import name

users = ["Вася", "Петя", "Маша", "Коша"]
scores = [95, 88, 79]

print("Список участников: ")
for number, name in enumerate(users, start=1):
    print(f"{number}: {name}")

print("Результаты по паре имя и оценка:")
for name , score in zip(users, scores):
    print(f"{name}: {score}")