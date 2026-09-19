name = input("привет, как тебя зовут ")
age = int(input("Сколько тетеб лет? "))
next_year_age = age + 1

print(f"привет, {name}! В следующем году тебе будет {next_year_age}")
print("привет, {0}! В следующем году тебе будет {1}".format(name, next_year_age))

next_year_string = "Привет, {name}! В следующем году тебе будет {next_year_age}"
print(next_year_string.format(name=name, next_year_age=next_year_age))