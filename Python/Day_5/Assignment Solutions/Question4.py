"""
Scenario
An AI classification pipeline processes raw data inputs. Each raw input is a tuple of string annotations describing a product name, 
its price, and rating. The pipeline needs to clean, filter, and sort these records.

Problem Description
Write a function process_dataset(dataset) that processes a dataset using built-in higher-order functions (map, filter) and lambda 
expressions:

dataset is a list of tuples containing string records. Example:
[("Laptop", "Price: 1200", "Rating: 4.8"), ("Phone", "Price: 800", "Rating: 4.5")]

Your pipeline must execute the following sequential steps:

Parsing: From the incoming raw tuples, extract the product name (string), numeric price (float), and rating (float). (You can use 
string splitting or RegEx to isolate the numeric values).

Filtering: Use filter() with a lambda function to keep only items with a parsed price less than or equal to 1000.0.
Mapping: Use map() with a lambda function to transform the filtered entries into dictionaries of the following structure: 
{"product": <name>, "price": <float_price>, "score": <float_rating>}.

Sorting: Sort the resulting list of dictionaries in descending order of their score using sorted() with a lambda key selector. 
If two items have the same score, their relative order does not matter.
The function should return the sorted list of dictionaries.
"""
import re
from pprint import pprint

def search_num(value, pattern):
    match = re.search(pattern, value)
    return match.group(0)


def process_dataset(dataset):
    result = []
    pattern = r"([0-9.]+)"

    valid_products = filter(lambda x: float(search_num(x[1], pattern)) <= 1000, dataset)
    result = map(lambda x: dict(product = x[0], price = float(search_num(x[1], pattern)), score = float(search_num(x[2], pattern))), valid_products)
    result = sorted(result, key = lambda x: x["score"])

    return result
        
def main():
    dataset = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
] 
    pprint(process_dataset(dataset))

if(__name__ == "__main__"):
    main()
