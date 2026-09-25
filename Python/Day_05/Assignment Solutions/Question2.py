# Scenario
# The CDAC academic portal needs to validate user registration submissions so that only valid academic emails ending in .edu or .res.in are registered.

# Problem Description
# Write a function validate_academic_email(email) that checks if a string is a valid academic email address using a regular expression.

# The email must satisfy the following syntax rules:
# Username: Must consist only of lowercase letters, numbers, dots, and underscores (a-z, 0-9, ., _). It must contain at least one character.
# Separator: Must contain exactly one @ symbol.
# Domain: Must consist of lowercase letters, numbers, dots, and hyphens (a-z, 0-9, ., -).
# Suffix: The domain must end with either .edu or .res.in (and nothing else).
# The regular expression must perform an exact match of the entire string (use boundary markers ^ and $).
# The function must return True if the email matches all criteria, and False otherwise.
import re
def  validate_academic_email(email):
    pattern = r"^[a-z0-9._]+@[a-z0-9.-]+(\.edu|\.res\.in)$"
    if not re.search(pattern, email):
        print("Please type a valid email")
        return False

    return True

def main():
    while(True):
        email = input("Enter Your Email: ")
        flag = validate_academic_email(email)
        if(flag == False):
            continue
        print("The Entered Email is valid")
        break
main()