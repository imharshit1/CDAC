from pprint import pprint
def print_inventory(inventory):
    print("Current Inventory: ")
    pprint(inventory)

def add_book(inventory, book_title, quantity):
    if book_title in inventory:
        inventory[book_title] += quantity
        printLine()
        print("The book already exists, so the quantity was updated")
        printLine()
    else:
        inventory[book_title] = quantity
        printLine()
        print("The book was added successfully")
        printLine()



def sell_book(inventory, book_title, quantity):
    if (book_title not in inventory):
        printLine()
        print("This book doesn't exist")
        printLine()

    elif (quantity > inventory[book_title]):
        printLine()
        print(f"Not enough books in inventory, Available: {inventory[book_title]}")
        printLine()
        return

    else: 
        inventory[book_title] -= quantity

        if (inventory[book_title]) == 0:
            del inventory[book_title]
            printLine()
            print("Quantity reached 0, so the book was deleted")
            printLine()
        else:
            printLine()
            print(f"{inventory[book_title]} books remain with this title")
            printLine()

    

def look_up(inventory, book_title):
    quantity = inventory.get(book_title, 0)
    
    if(quantity):
        printLine()
        print(f"there are {quantity} books with this title")
        printLine()
    else:
        printLine()
        print("This book doesn't exists")
        printLine()

    print_inventory(inventory)

def manage_bookstore_inventory(inventory, action, book_title,quantity=0):
    if(action == "1"): add_book(inventory, book_title, quantity)
    elif(action == "2"): sell_book(inventory, book_title, quantity)
    elif(action == "3"): look_up(inventory, book_title)
    
def printLine():
    print("-"*100)

def main():
    inventory = {}

    while(True):
        print("="* 100)
        print("Welcome to the bookstore inventory")
        print("="* 100)

        print()
        print("Type the mentioned numbers to perform the action")
        print()

        print("1. Add a book")
        print("2. Sell a book")
        print("3. Look for a book")
        print("Type anything to exits")

        print()
        action = input("Type the action you want us to do: ")
        print()
        if action != "1" and action != "2" and action != "3":
                    break
        
        book_title = input("Type the book title: ")
        print()

        if action in ("1", "2"):
            try:
                quantity = int(input("Type the quantity of books you want to add or remove: "))
                if (quantity <= 0):
                    printLine()
                    print("Quantity must be greater than 0")
                    printLine()
                    continue
                print()
            except ValueError:
                printLine()
                print("Invalid input, please type a number")
                printLine()
                continue

        manage_bookstore_inventory(inventory, action, book_title, quantity)

main()
