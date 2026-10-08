categories = []

categories.append("Python")
categories.append("Django")
categories.append("SQL")

print(categories)

categories.extend(["Git", "Docker"])
print(categories)

categories.insert(0, "Оглавление")
print(categories)
print(len(categories))

print("Django" in categories)

print(categories.count("Git"))
print(categories.index("Docker"))

first = categories.pop(0)
print(f"Мы удалили 0 элемент из списка {first}")
print(categories)

categories.remove("Git")
print(categories)
