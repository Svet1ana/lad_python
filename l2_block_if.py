from sysconfig import is_python_build

post_title = "Python"
post_text = "text"
is_published = True
is_draft = True

print(f"Post : {post_title}")

if is_published and not is_draft:
    print(f"Text : {post_text}")
elif is_draft:
    print(f" It is draft")
else:
    print(f" It is hide ")

guest_age = int(input("Guest Age : "))
is_adult_only = False
is_allow = True

if is_adult_only:
    # print("Text is visible" if guest_age >= 18 else "Text is not visible")
    if guest_age >= 18:
        print(f"{guest_age} years old. Text allowed")
    else:
        print("text not allowed")
else:
    print("text for all")