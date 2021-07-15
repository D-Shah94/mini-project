def main_menu():
    print("\nMain menu", "Choose option:", "[0] Exit", "[1] Products", sep = "\n")
    options = int(input("Enter number here: "))
    if options == 0:
        print("Goodbye")
        exit()
    elif options == 1:
        return(product_menu())
    else:
        print("\nEntry Error: Please try again") # maybe try and except here instead?
        return(main_menu())

def product_menu():
    print("\nProduct Menu","Choose option:", "[0] Return to Main Menu", "[1] Print Products", "[2] Add Product", "[3] Update Product", "[4] Delete Product", sep = "\n")
    options = int(input("Enter number here: "))
    if options == 0:
        return(main_menu())
    elif options == 1:
        print("\n", products)
        return(product_menu())
    elif options == 2:
        return(add_product())
    elif options == 3:
        return(update_product())
    elif options == 4:
        return(delete_product())
    else:
        print("\nEntry Error: Please try again")
        return(product_menu())

def add_product():
    new_product = str(input("Enter new product:"))
    products.append(new_product)
    print("\n", products)
    return(product_menu())

def update_product():
    print("\nChoose item to update:")
    print("[0] Return to Product Menu")
    for product in products:
        print(f"[{products.index(product) + 1}] {product}")
    options = (int(input("Enter number here: ")) - 1)
    if options == -1:
        return(product_menu())
    elif (options - 1) >= 0 and (options) < len(products):
        print(f"You have chosen: {products[options]}")
        updated_product = str(input("Enter updated product: "))
        products[options] = updated_product
        return(product_menu())
    else:
        print("\nEntry Error: Please try again")
        return(update_product())

def delete_product():
    print("\nChoose item to delete:")
    print("[0] Return to Product Menu")
    for product in products:
        print(f"[{products.index(product) + 1}] {product}")
    options = (int(input("Enter number here: ")) - 1)
    if options == -1:
        return(product_menu())
    elif (options - 1) >= 0 and (options) < len(products):
        print(f"You have chosen: {products[options]}. Are you sure you want to continue?")
        confirmation_dialogue = str(input("[Y] for yes, [N] for no: "))
        if confirmation_dialogue == "Y" or confirmation_dialogue == "y":
            print(f"You have deleted {products[options]}")
            products.remove(products[options])
            return(product_menu())
        elif confirmation_dialogue == "N" or confirmation_dialogue == "n":
            return(product_menu())
        else:
            print("\nEntry Error: Returning to Product Menu")
            return(product_menu())
    else:
        print("\nEntry Error: Please try again")
        return(product_menu())

products = ["coffee", "tea", "coke", "pepsi"]

main_menu()