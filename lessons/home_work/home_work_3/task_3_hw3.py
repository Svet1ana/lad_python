grades = [95, 88, 60, 42, 100]

for grade in grades:
    if grade >= 90:
        print(f"{grade} — exelent")
    elif grade >= 70:
        print(f"{grade} — good")
    elif grade >= 50:
        print(f"{grade} — not bad")
    else:
        print(f"{grade} — bad")