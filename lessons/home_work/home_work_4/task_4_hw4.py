def build_slug(title: str) -> str:
    result = title.lower()
    result = result.replace(" ", "-")

    clean = []
    for char in result:
        if char.isalnum() or char == "-":
            clean.append(char)
        else:
            clean.append("-")

    result = "".join(clean)

    while "--" in result:
        result = result.replace("--", "-")

    result = result.strip("-")
    return result


titles = [
    "Python for Beginners",
    "Python for PRO",
    "Wtat HTTP is?",
    "Strings in Python",
]

print("Titles with word 'Python':")
for title in titles:
    if "Python" in title:
        print(title)

print("Slug each titles:")
for title in titles:
    print(title, "-", build_slug(title))