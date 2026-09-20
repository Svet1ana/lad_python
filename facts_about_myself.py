birth_year = input("Write your birth year: ")
height = int(input("Write your height: "))
favorite_num = float(input("Write your favorite number: "))

def bool_love_python(love_python    ):
    answer = love_python.lower().strip()
    if answer in ["true", "yes", "да"]:
        return True
    elif answer in ["false", "no", "нет"]:
        return False
    else:
        return True

love_python = bool_love_python( input("Do you love python?: "))

print(birth_year, height, favorite_num, love_python)
print(type(birth_year), type(height), type(favorite_num), type(love_python))
