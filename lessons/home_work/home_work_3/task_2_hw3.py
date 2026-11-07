total = 0

while True:
    number = int(input("Enter number , 0 — finish: "))

    if number == 0:
        break

    total += number

print(f"Summ: {total}")