def printLine():
    print("-"*80)

def print_msg(msg):
    print()
    printLine()
    print(msg)
    printLine()
    print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_book_entry(catalog: list[dict], next_id: int) -> int:
    """Prompts user for book details, appends new dict, returns updated ID counter."""
    title = input("Enter the title of the book: ")
    author = input("Enter the name of the author: ")
    genre = input("Enter the genre of the book: ")

    while(True):
        try:
            price = int(input("Enter the price of the book: "))

            if(price < 0):
                print("The price of the book cannot be negative.")
                try_again = input("Do you want to try again? (yes/no): ")

                if(try_again.lower() == 'y' or try_again.lower == 'yes'):
                    continue

                else:
                    return

            break
        except:
            print("Invalid Input: The price of the book must be a Number. Try Again")
        
    while(True):
        try:
            copies = int(input("Enter the number of copies of the book: "))

            if(copies < 0):
                print("The number of copies of the book cannot be negative.")
                try_again = input("Do you want to try again? (yes/no): ")

                if(try_again.lower() == 'y' or try_again.lower == 'yes'):
                    continue

                else:
                    return

            break
        except:
            print("Invalid Input: The number of copies of the book must be a Number. Try Again")

    book_entry = dict(id = next_id, Book_Title = title, Author_Name = author, Price = price, Genre = genre, Copies = copies)
    next_id += 1
    catalog.append(book_entry)

    print()
    printLine()
    print("The book Entry is successfully created")
    printLine()
    print()
    # print(catalog)
    return next_id

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_one_product(catalog: list[dict]) -> None:
    id, name, author, genre, price, copies = catalog[0].values()
    print('---- Product Details ----')
    print(f'ID          : {id}')
    print(f'Name        : {name}')
    print(f'author      : {author}')
    print(f'Genre       : {genre}')
    print(f'Price       : {price}')
    print(f'Copies      : {copies}')

    print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_many_product(catalog: list[dict]) -> None:
    printLine()
    print(f'{'ID':^5}  {'Name':<15}  {'Author':<15}  {'Genre':<15}  {'Price':<10}  {'Copies':<10}')
    printLine()
    for entry in catalog:
        id, name, author, genre, price, copies = entry.values()
        print(f'{id:^5}  {name:<15}  {author:<15}  {genre:<15}  {price:<10}  {copies:<10}')
        printLine()
        print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_catalog(catalog: list[dict]) -> None:
    """Displays formatted tabular catalog or single-record card when count == 1."""
    print()
    if len(catalog) == 0:
        print_msg("Catalog is empty")
    elif(len(catalog) == 1):
        print_one_product(catalog)
    else:
        print_many_product(catalog)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def query_books(catalog: list[dict], search_term: str) -> list[dict]:
    """Returns filtered list matching ID or case-insensitive title/author substring."""
    flag = True
    if(type(search_term) == str): 
        search_term = search_term.lower()
        flag = False
    for entry in catalog:
        if(flag == True):
            if(entry["id"] == search_term):
                result = []
                result.append(entry)
                return result
        else:
            if(entry["Book_Title"].lower() == search_term or entry["Author_Name"].lower() == search_term):
                result = []
                result.append(entry)
                return result
    
    print_msg("NotFoundError: No entry was found")
    return []

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def modify_book_details(catalog: list[dict], book_id: int) -> bool:
    """Updates price and copies for the specified book ID; returns success status."""
    flag = False
    for entry in catalog:
        if(entry["id"] == book_id):
            price_choice = input("Type `yes` to change the price: ")
            if(price_choice.lower() == "yes" or price_choice.lower() == "y"):
                while(True):
                    try:
                        new_price = int(input("Enter the new price: "))
                        if(new_price < 0):
                            print("Price cannot be negative. Try again!")
                            continue
                        break
                    except:
                        print("Invalid Input: Price must be a integer value")
    
                entry["Price"] = new_price
                flag = True

            copies_choice = input("Type `yes` to change the number of copies: ")
            if(copies_choice.lower() == "yes" or copies_choice.lower() == "y"):
                while(True):
                    try:
                        new_copies = int(input("Enter the updated number of copies for the book: "))
                        if(new_copies < 0):
                            print("Number of copies cannot be negative. Try again!")
                            continue
                        break
                    except:
                        print("Invalid Input: Number of copies must be a integer value")
    
                entry["Copies"] = new_copies
                flag = True
    return flag

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def delete_book(catalog: list[dict]) -> None:
    while(True):
        try:
            id = int(input("Enter the id of the book: "))
            for entry in catalog:
                if(entry["id"] == id):
                    catalog.remove(entry)
                    print_msg("Entry successfully deleted")
                    return
            print_msg("Cannot the find the book with the given id")
            return
        except:
            print("Invalid input: id must be an integer value")

    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sync_catalog_to_file(filepath: str, catalog: list[dict]) -> None:
    """Serializes each book dictionary into pipe-delimited strings in write mode."""
    with open(filepath, "w", encoding="utf-8") as file:
        for entry in catalog:
            id, name, author, genre, price, copies = entry.values()
            file.write(f"{id} | {name} | {author} | {genre} | {price} | {copies}\n")



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def load_catalog_from_file(filepath: str) -> list[dict]:
    """Parses books.txt line-by-line using split('|') and reconstructs dictionary list."""

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_title():
    print("="*80)
    print("LIBRARY BOOK MANAGEMENT SYSTEM")
    print("="*80)
    print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_options():
    print()
    print("Enter a number from the following numbers to select the option")
    print()

    print("Options: ")
    print("1. Add Book")
    print("2. View Catalog")
    print("3. Search Books")
    print("4. Update Details")
    print("5. Delete Book")
    print("6. Save to File")
    print("7. Load from File")
    print("8. Exit")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def take_input():
    action = 8
    while(True):
        try:
            action = int(input("Enter the number: "))
            break
        except:
            print("Invalid Input: The input must be only numbers")

    return action

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def search_inputs(catalog: list[dict]) -> list[dict]:
    while(True):
        option = input("Enter 1 to search with id or 2 search with name or author: ")
        if(option == "1"):
            try:
                id = int(input("Enter the ID of the book: "))
                return query_books(catalog, id)
            except:
                print("ID must be an Integer Value")
        elif(option == "2"):
            name = input("Enter the name/author of the book: ")
            return query_books(catalog, name)
        else:
            print("Invalid input. Try again")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def modify_input(catalog: list[dict]) -> bool:
    while(True):
        try:
            id = int(input("Enter the ID: "))
            return modify_book_details(catalog, id)
        except:
            print("Invalid input: ID must be number, try Again")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    catalog = []
    next_id = 1
    while(True):
        print_title()
        print_options()

        action = take_input()

        match action:
                case 1:
                    next_id = add_book_entry(catalog, next_id)
                case 2:
                    render_catalog(catalog)
                case 3:
                    result = search_inputs(catalog)
                    render_catalog(result)
                case 4:
                    flag = modify_input(catalog)
                    if(flag):
                        print_msg("Entry is successfully modified")
                    else:
                        print_msg("Can't find the entry with the entered ID")
                case 5:
                    delete_book(catalog)
                case 6:
                    sync_catalog_to_file("practice_assessment_qp/Solutions/books.txt", catalog)
                case 7:
                    load_catalog_from_file()
                case 8:
                    exit()
                case _:
                    print("Invalid Option")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

if(__name__ == "__main__"):
    main()