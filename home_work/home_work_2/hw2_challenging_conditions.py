login = input("Please enter your login name: ")
password = input("Please enter your password: ")
age = int(input("Please enter your age: "))
email = input("Please enter your email: ")

if age > 18:
    print("You are older than your age.")
else:
    print(f"{age}, is less than or equal to 18")

