# Assignment 2: Robust Phonebook Contact Registry
# Scenario
# You are writing a Command-Line Interface (CLI) contact registry that maps user names to their phone
# numbers. The program needs to validate user inputs robustly to prevent corrupted formatting or empty
# values from breaking the registry database.

# Problem Description

# 1. Define a custom exception class named InvalidPhoneNumberError that inherits from
# Exception.

# 2. Write a function register_contact(phonebook, name, phone_input):
# phonebook is a dictionary mapping contact names (strings) to their phone numbers
# (strings).

# Validate the name parameter: it must be a non-empty string consisting only of alphabetic
# characters and spaces. If invalid, raise a standard ValueError with the message: "Contact
# name must be a non-empty alphabetic string."

# Validate the phone_input parameter: it must consist only of digits. Check this by
# attempting to convert it to an integer using int().

# If the conversion fails (raises a ValueError), catch that exception and raise your
# custom InvalidPhoneNumberError with the message: "Phone number must
# contain digits only."

# If validations pass, store phone_input as a string in the phonebook under the key name
# (preserving any leading zeros).

# Return the updated phonebook dictionary.
from pprint import pprint
def register_contact(phonebook, name, phone_input):
    phonebook[name] = phone_input

def main():
    phonebook = {}
    print("="*50)
    print("")
    while(True):
        print("Provide the following details: ")
        name = input("1. Name: ")
    
        if(name =="" or (int(name) == 0 or int(name))):
            print("ValueError: Contact name must be a non-empty alphabetic string. Try again!")
            continue
        try:
            phone_input = int(input("2. Phone number: "))
        except ValueError:
            print("InvalidPhoneNumberError: Phone number must consist only of digits. Try again!")
            continue
        phone_input = str(phone_input)
        register_contact(phonebook, name, phone_input)
        print("-"*50)
        print("Successfully added/updated the phone number")
        pprint(phonebook)
        print("-"*50)

        
main()
