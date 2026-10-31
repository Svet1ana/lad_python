def calculate():
    number = int(input("Input number: "))
    if number == 0:
        print(f"{number} is zero")
    if number < 0:
        print(f"{number} is negative number")
    if number > 0:
        print(f"{number} is positive number")
    if number % 2 == 0:
        print(f"{number} is even number")
    if number % 2 != 0:
        print(f"{number} is odd number")
    if number > 100:
        print(f"{number} is greater than 100")
    else:
        print(f"{number} is less than or equal to 100")

calculate()


def calc():
    number = int(input("Input number: "))
    if number == 0:
        print(f"{number} is zero")
    elif number < 0:
        print(f"{number} is negative number")
    elif number > 0:
        print(f"{number} is positive number")
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")
    if number > 100:
        print(f"{number} is greater than 100")
    else:
        print(f"{number} is less than 100")

calc()