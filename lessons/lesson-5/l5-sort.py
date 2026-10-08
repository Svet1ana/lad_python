prices = [4567, 3245, 4564, 5456]
prices.sort()
print(prices)

prices.sort(reverse=True)
print(prices)

prices.sort(key=lambda x: -x)
print(prices)


prices = [4567, 3245, 4564, 5456]
sorted_prices = sorted(prices)
print(f"Исходный список {prices}, отсортированный список {sorted_prices}")

print(f"Сумма всех элементов списка - {sum(sorted_prices)}")
print(f"Минимальный элемент в списке - {min(sorted_prices)}")
print(f"Максимальынй элемент в списке - {max(sorted_prices)}")

affordable = [number for number in prices if number <= 5000]
print(f"Доступные суммы {affordable}")

affordable = [number for number in sorted_prices if number <= 5000]
print(f"Доступные суммы {affordable}")

prices_strings = [str(price) for price in prices]
print(prices_strings)

affordable.reverse()
print(affordable)