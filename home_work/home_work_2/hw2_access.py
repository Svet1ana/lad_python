is_published = True
is_premium = True
text = "TEXT"
has_subscription = True

def access(text, is_premium, is_published, has_subscription):
    if is_published:
        if text != "" and (not is_premium or has_subscription):
            print(text)
        else:
            print("something is wrong ( post is premium )")
    else:
        print("Text is not published")

access(text, is_premium, is_published, has_subscription)

def access_short(text, is_premium, is_published, has_subscription):
    if is_published and text and (not is_premium or has_subscription):
            print(text)
    else:
            print("something is wrong")

access_short(text, is_premium, is_published, has_subscription)