# Assignment 4: Atomic E-Commerce Order Processor
# Scenario
# You are building an ordering subsystem for an online store. Orders containing multiple products must be
# processed atomically: either the entire order completes successfully, or the entire transaction fails. If
# one item in the order is out of stock or is unrecognized, no stock should be deducted for any other item
# (rollback).

# 1. Define two custom exceptions:
# ProductNotFoundError (raised when a product ID is not present in the catalog).
# OutOfStockError (raised when the customer's ordered quantity exceeds the available
# stock).   

# 2. Write a function process_order(catalog, order):
# catalog is a dictionary containing product database records. Format:
# catalog = {
#  "P01": {"price": 100.0, "stock": 5},
#  "P02": {"price": 50.0, "stock": 2}
# }
# order is a dictionary containing product IDs (keys) and quantities ordered (values). Format:
# {"P01": 2, "P02": 1}.

# Validation Phase: Before modifying any inventory levels:
# Check if all ordered keys exist in the catalog. If a product ID does not exist, raise

# ProductNotFoundError with message: "Product '<product_id>' not found in store catalog."

# Check if the catalog contains sufficient stock for each item ordered. If the ordered quantity exceeds available stock, 
# raise OutOfStockError with message: "Product
# '<product_id>' is out of stock. Requested: <requested_qty>,
# Available: <available_stock>."

# Execution Phase: If (and only if) all products pass validation:
# Deduct the ordered quantities from the stock numbers in the catalog dictionary.Calculate and return the total cost of the order (float).
# If an exception was raised during validation, the catalog must remain completely
# unchanged
from pprint import pprint

class ProductNotFoundError(Exception):
    pass

class OutOfStockError(Exception):
    pass

def validate(catalog, order):
    # Validation Phase
    for order_ID, order_quantity in order.items():

        # Check if product exists
        if order_ID not in catalog:
            raise ProductNotFoundError(
                f"Product '{order_ID}' not found in store catalog."
            )

        # Get available stock
        available_stock = catalog[order_ID]["stock"]

        # Check sufficient stock
        if order_quantity > available_stock:
            raise OutOfStockError(
                f"Product '{order_ID}' is out of stock. "
                f"Requested: {order_quantity}, "
                f"Available: {available_stock}."
            )


def process_order(catalog, order):
    
    validate(catalog, order)

    total_cost = 0.0

    for order_ID, order_quantity in order.items():
        product = catalog[order_ID]
        total_cost += product["price"] * order_quantity

        product["stock"] -= order_quantity

    return total_cost


def print_line():
    print("-" * 50)


def main():
    catalog = {
        "P01": {"price": 100.0, "stock": 5},
        "P02": {"price": 50.0, "stock": 2}
    }

    print("=" * 50)
    print(f"{'Atomic E-Commerce Order Processor':^50}")
    print("=" * 50)

    order = {}

    while True:
        try:
            n = int(input("Type the number of orders: "))
            if n <= 0:
                print_line()
                print("Number of orders must be greater than 0.")
                print_line()
                continue

        except ValueError:
            print_line()
            print("Invalid Input: Only type Integer value")
            print_line()
            continue

        break

    order_number = 1

    while order_number != n + 1:
        key = input(f"Order number {order_number}: Type the product ID: ")

        while True:
            try:
                value = int(
                    input("Type the quantity of the product: ")
                )

                if value <= 0:
                    print_line()
                    print("Quantity must be greater than 0.")
                    print_line()
                    continue

            except ValueError:
                print_line()
                print("Invalid Input: Only type Integer value")
                print_line()
                continue

            break

        order[key] = value
        order_number += 1

    try:
        total_cost = process_order(catalog, order)

        print_line()
        print("Transaction was successfully completed")
        print(f"Total Cost: ₹{total_cost:.2f}")
        print("Current Catalog:")
        pprint(catalog)
        print_line()

    except ProductNotFoundError as e:
        print_line()
        print(e)
        print("Transaction failed. No stock was deducted.")
        print_line()

    except OutOfStockError as e:
        print_line()
        print(e)
        print("Transaction failed. No stock was deducted.")
        print_line()


main()
