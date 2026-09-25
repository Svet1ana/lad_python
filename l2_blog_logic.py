post_text = "1"
is_published = True
is_premium = False
has_subscription = False

print("есть ли статься для отоброажения: ", bool(post_text))

can_show = post_text and is_published and ( is_premium or has_subscription )

if can_show:
    print(f"Показываем тектс: {post_text}")
else:
    print("NO")

arthur_name = input("name : ")
display_name = arthur_name or "no_name"

print(f"Arthur Name : {display_name}")

age = int(input("age : "))
if 0 <= age > 100:
    print("ok")
else:
    print("no")