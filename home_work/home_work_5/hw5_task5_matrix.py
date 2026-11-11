"""
Звёздочка (вложенные списки / матрица). Создайте матрицу 3×4 — список из трёх строк по четыре числа.
Выведите: а) сумму всех элементов; б) сумму элементов в каждой строке; в) максимальный элемент во всей матрице;
г) «транспонированную» матрицу (строки и столбцы поменять местами) — разберитесь самостоятельно,
как это сделать через вложенные циклы и comprehension.
"""

matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
]

row_sums = [sum(row) for row in matrix]
total = sum(row_sums)
largest = max(max(row) for row in matrix)

print(f"Sum all elementes: {total}" )
print(f"Sum of row : {row_sums}")
print(f"Max: {largest}" )

transposed = []

for col in range(len(matrix[0])):
    new_row = []

    for row in matrix:
        new_row.append(row[col])

    transposed.append(new_row)

print(transposed)

transposed_comprehension = [
    [row[col] for row in matrix]
    for col in range(len(matrix[0]))
]
print(transposed_comprehension)