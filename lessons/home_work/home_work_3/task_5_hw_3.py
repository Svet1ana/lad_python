numbers = [4, 9, 15, 23, 42]
target = int(input("What number is looking for? "))


for number in numbers:
    if number == target:
        print("Find")
        break
else:
    print("Not find")