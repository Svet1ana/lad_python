text = "Это текст с лишними пробелами"
words = text.split()
print(words)

print(f"Слов в тексте: {len(words)}")

longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)

new_text = " ".join(words)
print(new_text)


normalized = "-".join(text.split())
print(normalized)

normalized2  = " | ".join(text.split())
print(normalized2)

print(f"Символы до очистки: {len(text )}")