name = input("What is your name? ")
age = int(input("How old are you? "))
next_year_age = age + 1
second = None

print(f"Hello, {name}! In the next year you will be {next_year_age}")
print("Hello, {0}! In the next year you will be  {1}".format(name, next_year_age))

next_year_string = "Hello, {name}! In the next year you will be {next_year_age}".format(name=name, next_year_age=next_year_age)
print(next_year_string)


print(f"привет , {name} ! как утебя дела? я слышал , что тебе на будущий год будет {next_year_age}")
print("привет, {0}! в следующем году тебе будет {2}".format(name, second, next_year_age))