def add(a: int, b: int) -> int:
    """Возвращате сумму двух чисел"""
    return a + b
def print_sum(a: int, b: int) -> None:
    """Выводит сумму сложения , но не возращает ее"""
    print(f" сумма: {a + b}")


def show_message() -> None:
    print(message)
    
def make_local() -> None:
    message = "Локальная"
    print(message)


message = "глобальная"
result=print_sum(50 , 10)
print(result)

total = add(5, 9)
print(total)

show_message()

make_local()
print(message)

counter = 0

def increment() -> None:
    global counter
    counter += 1

increment()
increment()

print(counter)





