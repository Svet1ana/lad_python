rating = float(input("Specify the movie rating: "))

# миниумм условий проверки , что позвоялет сделать краткую запись вида -
verdict = "рекомендую" if rating >= 7 else "пропустить"
print(verdict)

def verdict2str(verdict):
    rating_def = float(input("Specify the movie rating: "))
    verdict_def = "рекомендую" if rating_def >=7 else "пропустить"
    return verdict_def

print(verdict2str(verdict))