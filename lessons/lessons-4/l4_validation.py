row_age = (input("What is your age?: ")).strip()
if row_age.isdigit():
    row_age = int(row_age)
    print(row_age)

else:
    print("Age must be an integer")

login = (input("What is your login?: ")).strip()
if login and login.isalnum():
    print(login)
else:
    print("Login must be alphanumeric")

full_name = (input("What is your full name?: ")).strip()
parts = full_name.split(" ")
print(parts)
if len(parts) == 3:
    surname, name, midlename = parts
    print(surname)
    print(name)
    print(midlename)
    print(f"surname - {surname}, name - {name}, midlename - {midlename}")
else:
    print("Invalid input")
# if full_name and full_name.isalpha():
#     print(full_name)
# else:
#     print("Full name must be alpha")