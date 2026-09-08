# Assignment 3: Corporate Directory Search & Scraper
# Scenario
# You are writing a parser to extract formatted employee phone records from unstructured text files. Employee phone numbers are formatted in multiple ways across the directory.

# Problem Description
# Write a function scrape_directory_phones(directory_text) that extracts phone records from text and returns a structured list of dictionaries.

# The function must detect phone numbers matching any of the following three formats:
# AAA-PPP-LLLL (e.g., 123-456-7890)
# (AAA) PPP-LLLL (e.g., (123) 456-7890)
# AAAPPPLLLL (10 consecutive digits, e.g., 1234567890) where AAA represents the area code (3 digits), PPP represents the prefix (3 digits), and LLLL represents the line number (4 digits).
# Design a single compiled RegEx pattern to parse all three formats using capture groups.
# For each match found in directory_text, build a dictionary with the following keys:
# "area_code": String containing the extracted 3 area code digits.
# "prefix": String containing the extracted 3 prefix digits.
# "line_number": String containing the extracted 4 line number digits.
# "formatted": A normalized phone string in the format "(AAA) PPP-LLLL".
# Return a list of these dictionaries. If no phone numbers are found, return an empty list.
import re
from pprint import pprint
def scrape_directory_phones(directory_text):
    pattern = re.compile(r"(?:\(([0-9]{3})\) ([0-9]{3})-([0-9]{4})|"
                         r"([0-9]{3})-([0-9]{3})-([0-9]{4})|"
                         r"([0-9]{3})([0-9]{3})([0-9]{4}))")

    result = []

    while(True):
        match = re.search(pattern, directory_text)
        if(not match):
            break

        if(match.group(1)):

            area_code = match.group(1)
            prefix = match.group(2)
            line_number = match.group(3)

        elif(match.group(4)):

            area_code = match.group(4)
            prefix = match.group(5)
            line_number = match.group(6)

        else:
            area_code = match.group(7)
            prefix = match.group(8)
            line_number = match.group(9)

        formatted = f"({area_code}) {prefix}-{line_number}"
        result.append(dict(area_code = area_code, prefix = prefix, line_number = line_number, formatted = formatted))
        directory_text = directory_text[match.end():]
        

    return result



def main():
    directory_text = input("Enter the directory: ")
    result = scrape_directory_phones(directory_text)
    if(result == []):
        print("No search is found")
    else:
        pprint(result)

if(__name__ == "__main__"):
    main()
