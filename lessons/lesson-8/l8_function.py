def greet(name: str) -> None:
    """Выводит приветствие по имени"""
    print(f"Hello, {name}!")


def user_info(name: str, age: int) -> None:
    """выводит имя и возраст пользователя"""
    print(f"Hello, {name}, you are {age} years old!")


def greet_full(name: str, greeting: str = "Привет") -> None:
    print(f"{greeting} {name}!")


greet_full("Leo")

greet_full("Ivan", greeting="Hello")

greet("Masha")

greet(name="Bob")

user_info("Bob", 18)

user_info(age=21, name="Ivan")

