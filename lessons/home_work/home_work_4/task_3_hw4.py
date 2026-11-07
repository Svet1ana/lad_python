def is_palindrome(text):
    chars = []

    for char in text.lower():
        if char.isalnum():
            chars.append(char)

    cleaned = "".join(chars)
    return cleaned == cleaned[::-1]


print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("А роза, упала на лапу Азора!"))
print(is_palindrome("palindrome"))