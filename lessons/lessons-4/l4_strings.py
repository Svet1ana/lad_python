title = "Заголовок"

print(title[4])
print(title[-2])
print(title[0])
print(title[6:])
print(title[2:6])
print(title[-8:])
print(title[::-1])

print(title.upper())
print(title.title())
print(title.lower())

dirty = "  dirty ! . "
clean = dirty.strip("!. ")
print(clean)
print(f"Длина до strip {len(dirty)} , после strip {len(clean)}")

print(title.replace("Заго", "У"))
print(title.replace("о", "Ы"))

# empty_string = ""
# print(empty_string[0])

print(title.startswith("З"), title.endswith("к"))

print(title.find("г"))

print(title.count("о"))


