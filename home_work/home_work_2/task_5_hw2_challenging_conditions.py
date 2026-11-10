login = input("Please enter your login : ").strip()
password = input("Please enter your password: ")
age = int(input("Please enter your age: "))
email = input("Please enter your email: ").strip()

has_erroors = False

if not login or len(login) <= 1:
    print("Error.You are not logged in.")
    has_erroors = True

if not password or len(password) < 8:
    print("Error. Password is too short.")
    has_erroors = True

if age < 18:
    print(f"{age}, is less than or equal to 18.")
    has_erroors = True

email_is_valid = (
    email.count("@") == 1
    and "." in email
    and " " in email

)

if not email_is_valid:
    print(f"{email}, is an invalid email address.")
    has_erroors = True

if not has_erroors:
    print(f"{login}, {password}, {age}, {email} are valid.")
    has_erroors = True