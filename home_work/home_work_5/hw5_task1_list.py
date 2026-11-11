"""
Список чисел и статистика.
Создайте список из 6–8 чисел (например, баллы за тест).
Выведите сумму (sum),
минимальное и максимальное значение,
среднее (сумма / длина) и список,
отсортированный по убыванию.
"""
scores = [80, 95, 70, 100, 85, 50]

total = sum(scores)
print(f"Sum of scores = {total}")

average = total / len(scores)
print(f"Average score = {average}")

print("Min score:", min(scores))
print("Max score:", max(scores))

descending = sorted(scores, reverse=True)
print(f"Descending score = {descending}")