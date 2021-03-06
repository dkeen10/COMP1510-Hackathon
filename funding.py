"""
Functions to verify if a user is qualified for CERB funding.
"""
# Verify country, age, income, student, province
import time
import webbrowser
import user
import doctest


def verify_for_funding(user_object: object):
    """
    Verify user for Canada's government funding.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Correctly verify if user_object is verified for government funding
    """
    # This dictionary is used to store Boolean values received from object attribute value verification functions
    keys = ["Country", "Age", "Income"]
    values = [verify_country(user_object), verify_age(user_object), verify_income(user_object)]

    # Dictionary comprehension
    verification = {keys[i]: values[i] for i in range(len(keys))}

    # If every value in the verification dictionary is true, it will do the following:
    if all(value for value in verification.values()):
        print("You are verified for funding! "
              "Please follow the instructions in the link that will open in your browser.\n")

        # After two seconds, the user's default browser will be launched to the CERB page on canada.ca
        time.sleep(2)
        open_link("https://www.canada.ca/en/revenue-agency/services/benefits/apply-for-cerb-with-cra.html")

    else:
        print("Unfortunately, you do not appear to qualify for the CERB funding. You must be of at least 15 years of"
              " age, have made at least $5000 in the past year, and be a Canadian resident.\n")

        # The below input stalls the screen so users can read before the main menu appears again
        input("Hit enter to continue")


def verify_country(user_object: object) -> bool:
    """
    Verify user's country.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Correctly verify if user_object's country is Canada

    :return: A boolean if user_object's country is Canada

    >>> user_object = user.User("Jessica Hong", 23, 35000, "Canada", True)
    >>> verify_country(user_object)
    True

    >>> user_object = user.User("Jessica Hong", 23, 0, "United States", False)
    >>> verify_country(user_object)
    False
    """
    # Return true if the Country value in a User object is "Canada'
    return True if user_object.get_country() == "Canada" else False


def verify_age(user_object: object) -> bool:
    """
    Verify user's age.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Correctly verify if user_object's age is 15 or more (Age of qualification for CERB funding)

    :return: A boolean if user_object's age is 15 or more

    >>> user_object = user.User("Jessica Hong", 15, 35000, "Canada", True)
    >>> verify_age(user_object)
    True

    >>> user_object = user.User("Jessica Hong", 0, 0, "United States", False)
    >>> verify_age(user_object)
    False
    """
    # Return true if the Age value in a User object is greater than 15
    return True if user_object.get_age() >= 15 else False


def verify_income(user_object: object) -> bool:
    """
    Verify user's income status.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Correctly verify if user_object's income is 5000 or more (CERB minimum requirement)

    :return: A boolean if income is more than 5000, otherwise invoke verify_if_student function

    >>> user_object = user.User("Jessica Hong", 15, 35000, "Canada", True)
    >>> verify_income(user_object)
    True
    """
    # Check to see if user meets the CERB threshold for annual income
    if user_object.get_income() >= 5000:
        return True

    # If the user is below the CERB threshold, we will check to see if they qualify for BC emergency student funds
    else:
        verify_if_student(user_object)


def verify_if_student(user_object: object):
    """
    Verify if user is a post-secondary student.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Will successfully invoke verify_province function if user is a student, otherwise print a
    rejection message
    """
    #  If the user is a student, ask them which Province/Territory they are in
    if user_object.get_student():
        verify_province()

    #  If they are not a student, print a sad message :(
    else:
        return


def verify_province():
    """
    Verify if user's province is British Columbia.

    :precondition: User's input must be a string
    :postcondition: Correctly verify if user's province is British Columbia
    :raise ValueError if the user enters an empty string when prompted for input
    """
    try:
        # Ask user for their Province or Territory
        user_province = province_selector()

        # If the user enters an empty string, raise a ValueError
        if user_province == "":
            raise ValueError

    # Catch the ValueError that may be risen in the try
    except ValueError:
        print("A province or territory name cannot be blank, please try again")

    else:
        # If the user entered British Columbia in some capacity, open a link to the emergency funding on gov.bc.ca
        if user_province == "BRITISH COLUMBIA" or user_province == "BC":

            print("Because you are a post-secondary student, BC's government is offering you emergency support. "
                  "A link has been opened in your browser for your educational viewing.")

            time.sleep(2)  # Wait two seconds before opening the link to provide time for user to digest the message
            open_link("https://news.gov.bc.ca/releases/2020AEST0018-000615")

        else:
            return


def province_selector():
    """
    Select a province or territory.

    :precondition: User enters in the correct province or territory
    :postcondition: Will return the user selection

    :return: User province/territory as a string in uppercase
    """
    #  A tuple containing all of the Canadian provinces and territories
    provinces_and_territories = ("Alberta", "British Columbia", "Saskatchewan", "Manitoba", "Ontario", "Quebec",
                                 "New Brunswick", "Nova Scotia", "Prince Edward Island", "Newfoundland", "Nunavut",
                                 "Northwest Territories", "Yukon")

    # Prepare the user for input request
    print("Which province or territory do you live in?")

    # Use a for loop to iterate through the range of the tuple and print each index in the tuple for viewing pleasure
    for i in range(len(provinces_and_territories)):
        print(provinces_and_territories[i])

    # Ask which province/territory user lives in
    user_province = input("Enter your response either in the fullname or acronym "
                          "(ex. British Columbia or BC): ").upper().strip()

    return user_province


def open_link(url: str):
    """
    Open the article URL in user's default web browser.

    :param url: A string
    :precondition: url must be a well-formed string
    :postcondition: Successfully open the article URL in user's default web browser
    """
    webbrowser.open_new(url)


def main():
    """
    Test the functions in the module.
    """
    doctest.testmod()


if __name__ == '__main__':
    main()
