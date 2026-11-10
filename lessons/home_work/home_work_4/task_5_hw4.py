def is_valid_email(email):
    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    if not local or not domain:
        return False

    for char in email:
        if char.isspace():
            return False

    if "." not in domain or domain.endswith("."):
        return False

    domain_parts = domain.split(".")
    if "" in domain_parts:
        return False

    suffix = domain_parts[-1]
    return len(suffix) >= 2 and suffix.isalpha()


print(is_valid_email("sveta@example.ru"))     # True
print(is_valid_email("prog@blog.example.dev"))  # True
print(is_valid_email("sveta@@example.ru"))    # False: два @
print(is_valid_email("@example.ru"))          # False: пусто слева
print(is_valid_email("sveta@example"))        # False: нет точки
print(is_valid_email("sveta@example.r"))      # False: одна буква
print(is_valid_email("sveta@example.r2"))     # False: в суффиксе цифра