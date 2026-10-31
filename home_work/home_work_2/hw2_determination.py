def determine_age_group():

    age = int(input("What is your age? "))

    if age >=0 and age <= 12:
        print("Children")
    elif age >=13 and age <= 17:
        print("Teenager")
    elif age >=18 and age <= 64:
        print("Adult")
    elif age >=65 and age <= 150:
        print("Pensioner")
    elif age <0 or age > 150:
        print("Error")
    else:
        print("Very Good")

determine_age_group()

def age_group():
    try:
        age = int(input("What is your age? "))
    except ValueError:
        print("Error bla=bla numeric")
        return

    if 0 <= age <=12:
        print("Child")
    elif 13 <= age <= 17:
        print("Teenager")
    elif 18 <= age <= 64:
        print("Adult")
    elif 65 <= age <= 150:
        print("Pensioner")
    elif age < 0 or age > 150:
        print("Error")

age_group()
