while True:
    try:
        first_number = int(input("Enter first number : "))
        second_number = int(input("Enter second number : "))
        result = first_number // second_number
    except ZeroDivisionError:
        print("Invalid operation = / 0. we will // 10.")
        result = first_number // 10

    except ValueError:
        print("Invalid input. Try again.")
        continue

    else:
        print("number is valid.")

    finally:
        print(f"result = {result}")

    break



