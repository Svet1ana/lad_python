"""
Цены и «доступность». Дан список цен. Порог вводится с клавиатуры.
Через comprehension постройте список флагов True/False — цена меньше порога.
Посчитайте, сколько цен ниже порога (sum(flags)), и выведите среднюю цену только по «доступным» позициям.
"""

prices = [100, 250, 500, 750]
threshold = float(input("Enter price: "))

flags = [price < threshold for price in prices]
available_prices = [price for price in prices if price < threshold]

count = sum(flags)

print("Flags:", flags)
print("Count:", count)

if count > 0:
    average = sum(available_prices) / count
    print("Average :", average)
else:
    print("Not available.")