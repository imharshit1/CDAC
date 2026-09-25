def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):
    total = base_price

    for item in items:
        total += item

    discounted_price = total * ((100 - discount) / 100)
    tax = discounted_price * tax_rate
    final_total = discounted_price + tax + delivery_fee

    return final_total


def get_number(prompt, min_value=0):
    while True:
        try:
            value = float(input(prompt))

            if value < min_value:
                print(f"Value cannot be less than {min_value}. Try again!")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_tax_rate():
    while True:
        tax_rate = get_number("Enter the new tax rate (0-1): ")

        if tax_rate <= 1:
            return tax_rate

        print("Tax rate should be between 0 and 1. Try again!")


def get_discount():
    while True:
        discount = get_number("Enter the discount (0-100): ")

        if discount <= 100:
            return discount

        print("Discount should be between 0 and 100. Try again!")


def main():
    print("=" * 50)
    print("Cafeteria Bill Calculator")
    print("=" * 50)
    
    base_price = get_number("Enter the BASE PRICE of MAIN COMBO MEAL: ")

    count_side_dishes = int(get_number("Enter the number of side dishes: "))

    items = []

    for i in range(1, count_side_dishes + 1):
        price = get_number(f"Enter the price of side dish number {i}: ")
        items.append(price)

    flag = input("Type 'yes' if there is any change in tax rate or type anything if there is no change: ").lower()

    tax_rate = 0.05

    if flag in ("yes", "y"):
        tax_rate = get_tax_rate()

    discount = get_discount()

    delivery_fee = get_number("Enter the Delivery Fee: ")

    final_total = calculate_cafeteria_bill( base_price, *items, tax_rate=tax_rate, discount=discount, delivery_fee=delivery_fee)

    print("=" * 50)
    print(f"Final Total: {final_total:.2f}")
    print("=" * 50)


main()
