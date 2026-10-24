import csv

rows = [
    ["title", "author", "views"],
    ["Cosmos", "Perelman", 120],
    ["Math", "Perelman", 150],
    ["Geo", "Perelman", 150]
]


with open("articels.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("articels.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)