from random import randint


secret = randint(1, 11)
attempts = 0
while True:
    guess = int(input("What is your guess? "))
    attempts += 1

    if guess < secret:
        print(f"{guess} is too low")
        continue

    if guess > secret:
        print(f"{guess} is too high")
        continue

    if guess == secret:
        print(f"{guess} is correct, {attempts} attempts")
        break