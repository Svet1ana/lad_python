from asyncio import events
from sys import flags

numbers = list(range(1, 11))
print(numbers)

squares = [number ** 2 for number in numbers]
print(f"Квадраты: {squares}")

evens = [number for number in numbers if number % 2 == 0]
print(f"Четные% {evens}")


prices = [4567, 3245, 4564, 5456]
flags = [number > 5000 for number in prices]

print(prices, flags, sep='\n')

categories = ['Python', 'Django', 'SQL', 'Git', 'Docker']
titles = [word.capitalize() if word != 'SQL' else word.upper() for word in categories ]
print(titles)