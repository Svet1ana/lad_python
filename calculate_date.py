def calculate_count_days():
    while True:
        try:
            age = input("What is your age?: ")
            count  = int(age) * 365
            return count
        except ValueError:
            print("Ошибка! Вы ввели не число. Пожалуйста, используйте только цифры.")

count_days = calculate_count_days()
print(f"Count of days = {count_days}")
