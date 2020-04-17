"""
Functions that assist in generating a User object.
"""
import doctest
import user
import re


def create_user():
    name = enter_name()
    age = enter_age()
    income = enter_income()
    country = enter_country()
    student_status = is_student()

    return user.User(name, age, income, country, student_status)


def enter_name():
    sentinel = False
    while not sentinel:
        name = input("What is your first and last name? (ex. Chris Thompson): ").strip()
        sentinel = validate_name(name)

    print("Pleasure to meet you, %s." % name)
    return name


def validate_name(name):
    name_regex = re.compile(r'^[A-Z][a-zA-Z]* [A-Z][a-zA-Z]*$')  # First name starts with a capital then any letter
    match_object = name_regex.search(name)

    return True if match_object else False


def enter_age():
    while True:
        try:
            age = int(input("What is your current age?: "))

            if age <= 0:
                raise ValueError

        except ValueError:
            print("Please enter your age as a positive integer.")

        else:
            return age


def enter_income():
    while True:
        try:
            income = int(input("What is your current annual income? (Enter your income as a positive integer): "))

            if income <= 0:
                raise ValueError

        except ValueError:
            print("Please enter your income as a positive integer.")

        else:
            return income


def enter_country():
    country = input("What is your country of residence?: ")
    return country.strip().title()


def is_student():
    options = ["Yes", "No"]

    print("Are you a current post-secondary student?")
    for i, thing in enumerate(options):
        print("%d: %s" % (i + 1, thing))

    while True:
        user_input = input()
        if user_input == "1":
            return True

        elif user_input == "2":
            return False

        else:
            print("Please enter 1 or 2.")


def check_if_user_information_is_correct(user_oject):
    return None


def main():
    doctest.testmod()
    print("Welcome!")
    new_user = create_user()



if __name__ == '__main__':
    main()