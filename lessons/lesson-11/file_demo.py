file = open("Notes.txt", "w", encoding="utf-8")
file.write("My first note \n" )
file.write("My second note \n" )
file.close()


with open("Notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)

with open("Notes.txt", "a", encoding="utf-8") as file:
    file.write("My Third note \n" )

with open("Notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Строка: {line.strip()}")