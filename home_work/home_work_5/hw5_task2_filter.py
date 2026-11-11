"""
Фильтрация строк через comprehension.
Заведите список из 8–10 строк (например, названий категорий блога).
Через list comprehension:
а) отфильтруйте строки длиннее 5 символов;
б) постройте список из длин всех строк (len);
в) постройте список строк с первой буквой в верхнем регистре (capitalize()).
Выведите каждый результат.
"""
categories = ["Code", "python", "news", "test", "datat", "blog", "web"]

long_categories = []
for name in categories:
    if len(name) > 5:
        long_categories.append(name)

print(long_categories)

long_cat = [name for name in categories if len(name) > 3]
print(long_cat)

lengths = [len(name) for name in categories]
print(lengths)


capitalized = [name.capitalize() for name in categories]
print(capitalized)