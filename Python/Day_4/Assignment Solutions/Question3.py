# Assignment 3: Course Feedback Compiler & Sanitizer Scenario
# Student feedback records contain ratings from 1 to 5 stars. Due to raw data entry issues, the feedback
# database has some course entries with list values that are empty, or lists containing invalid elements
# (such as string annotations like "Excellent" or None values).

# Problem Description
# Write a function compile_feedback(ratings_dict) that processes course feedback:

# The parameter ratings_dict is a dictionary where keys are course names (strings) and values
# are lists of ratings (which should be numeric but may contain invalid types).

# The function must return a dictionary mapping each course name to its average rating, rounded to
# 2 decimal places.

# Implement the following error handling criteria:

# 1. For each rating inside a course's list, attempt to convert it to a float. If a rating cannot be
# converted (throws a ValueError or TypeError), catch the exception, print a warning:
# "Warning: Invalid rating value '<val>' in course '<course>' skipped.",
# and continue processing the rest of the list.

# 2. If a course has no valid ratings (the list is empty or contains no convertible numbers),
# computing the average will trigger a division-by-zero error. Catch ZeroDivisionError,
# print a warning: "Warning: No valid ratings found for course '<course>'.
# Rating set to 0.0.", and assign the course an average rating of 0.0.

from pprint import pprint
def calculate_average_rating(feedback_data):
    for key, value in feedback_data.items():
        sum = 0

        length = len(value)
        if(length == 0):
            print(f"Warning: No valid ratings found for course '{key}'. Rating set to 0.0.")
            continue

        average = 0.0

        for rating in value:
            try:
                converted_rating = float(rating)
                sum += converted_rating

            except TypeError:
                print(f"Warning: Invalid rating value '{rating}' in course '{key}' skipped.")
                length -= 1
                continue
            except ValueError:
                print(f"Warning: Invalid rating value '{rating}' in course '{key}' skipped.")
                length -= 1
                continue

        if(length == 0):
            feedback_data[key] = 0.0    
        else :
            average = sum / length
            feedback_data[key] = average
    
def main():
    feedback_data = {
        "Python Programming": [5, 4, "4", "Great", 5],
        "Machine Learning": [],
        "Deep Learning": ["Good", "Average", None]
    }

    calculate_average_rating(feedback_data)
    pprint(feedback_data)


main()