def printLine():
    print("-"*100)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def big_print(string):
    printLine()
    print(string)
    printLine()
    print()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_title(title):
    print("="*100)
    print(title)
    print("="*100)
    print()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_menu():   
    print("Menu:")
    print(f"1. Add Product\n"
            f"2. View All Products\n"
            f"3. Search Product \n"
            f"4. Update Product \n"
            f"5. Delete Product \n"
            f"6. Exit")
    printLine()
    print()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def float_input(value: str) -> float:
    while(True):
        try:
            user_input = float(input(f"Enter the {value} of the product: "))
            if(user_input < 0):
                print(f"The {value} cannot be negative.")
                continue

            return user_input
        except ValueError:
            print(f"Invalid input: {value} must be a number.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def int_input(value: str) -> int:
    while(True):
        try:
            user_input = int(input(f"Enter the {value} of the product: "))
            if(user_input < 0):
                print(f"The {value} cannot be negative.")
                continue

            return user_input
        except ValueError:
            print(f"Invalid input: {value} can only be an Integer value.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_product(product: list[dict], next_id: int) -> int:

    name = input("Enter the Name of the Product: ")
    category = input("Enter the Category of the Product: ")
    price = float_input("price")
    quantity = int_input("quantity")

    product.append(dict(id = next_id, name = name, category = category, price = price, quantity = quantity))
    big_print(f"Product added Successfully, your product's ID is: {next_id}")
    next_id += 1
    return next_id

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_one(product):
    id, name, category, price, quantity = product[0].values()
    print('---- Product Details ----')
    print(f'ID          : {id}')
    print(f'Name        : {name}')
    print(f'Category    : {category}')
    print(f'Price       : {price}')
    print(f'Quantity    : {quantity}')
    printLine()
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_many(product):
    printLine()
    print(f"{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}")
    printLine()
    for p in product:
        id, name, category, price, quantity = p.values()
        print(f'{id:^5}{name:<20}{category:<20}{price:>10.2f}{quantity:>5}')
    printLine()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_product(product):
    if(len(product) == 0):
        print()
        big_print("Product list is empty")
    elif(len(product) == 1):
        print_one(product)
    else:
        print_many(product)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def search_product(product):
    id = int_input("ID")
    for p in product:
        if(p["id"] == id):
            return [p]
    big_print("Product with this ID not found")
    return []

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update(product : dict) -> bool:
    print("Leave blank if you do not want to change")
    flag = False
    new_name = input("Enter the new name: ")
    if(new_name != ""): 
        product["name"] = new_name
        flag = True

    new_category = input("Enter the new Category of the product: ")
    if(new_category != ""): 
        product["category"] = new_category
        flag = True

    while(True):
        new_price = input("Enter the new price: ")
        if(new_price == ""):
            break
        else: 
            try:
                new_price = float(new_price)
                if(new_price < 0):
                    print("Price cannot be negative")
                    continue

                product["price"] = new_price
                flag = True
                break

            except ValueError:
                print("Invalid input: Price must be a number")

    while(True):
        new_quantity = input("Enter the quantity of the product: ")
        if(new_quantity == ""):
            break
        else: 
            try:
                new_quantity = int(new_quantity)
                if(new_quantity< 0):
                    print("Quantity cannot be negative")
                    continue

                product["quantity"] = new_quantity
                flag = True
                break

            except ValueError:
                print("Invalid input: Quantity must be a number")

    return flag

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_product(product):
    product_id  = int_input("ID")
    for p in product:
        if(p["id"] == product_id):
            return update(p)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def delete_product(product):
    product_id = int_input("id")
    flag = False
    for p in product:
        if(p["id"] == product_id):
            product.remove(p)
            flag = True
            break

    if(flag == True):
        big_print("The product is successfully deleted")
    else:
        big_print("The product with this id doesn't exist")    

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    product = []
    next_id = 1
    while(True):
        print_title("Product Inventory Managment System")
        big_print("Press the following numbers to select the option")
        print_menu()
        user_choice = input("Enter the number: ")

        match user_choice:
            case "1":
                next_id = add_product(product, next_id)
            case "2":
                view_product(product)
            case "3":
                result = search_product(product)
                if(result != []): view_product(result)
            case "4":
                flag = update_product(product)
                if(flag):
                    big_print("Product is successfully updated")
                else:
                    big_print("Cannot find the product with the given ID")
            case "5":
                delete_product(product)
            case "6":
                exit()
            case _:
                big_print("Invalid Input.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
if(__name__ == "__main__"):
    main()