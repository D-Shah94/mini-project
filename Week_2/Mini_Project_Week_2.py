def import_products():
        with open("products.txt", "r") as file1:
            for i in file1:
                products.append(i.strip("\n"))

def import_couriers():
        with open("couriers.txt", "r") as file1:
            for i in file1:
                couriers.append(i.strip("\n"))


def main_menu():
    print("\nMain menu", "Choose option:", "[0] Save and Exit", "[1] Products","[2] Courier", sep = "\n")
    options = int(input("Enter number here: "))
    if options == 0:
        print("Goodbye")
        exit()
    elif options == 1:
        return(product_menu())
    elif options == 2:
        return(courier_menu())
    else:
        print("\nEntry Error: Please try again") # maybe try and except here instead? / change numbers to strings
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

# 
    

# (view lists in top menu function) 
# Create a function within a function in order to easily use product_menu() and courier menu() with the same code?
# (watch out for elifs at stop could conflict with changes) 

def courier_menu():
    print("\nCourier Menu","Choose option:", "[0] Return to Main Menu", "[1] Print Couriers", "[2] Add Courier", "[3] Update Courier", "[4] Delete Courier", sep = "\n")
    options = int(input("Enter number here: "))
    if options == 0:
        return(main_menu())
    elif options == 1:
        print("\n", couriers)
        return(courier_menu())
    elif options == 2:
        return(add_courier())
    elif options == 3:
        return(update_courier())
    elif options == 4:
        return(delete_courier())
    else:
        print("\nEntry Error: Please try again")
        return(product_menu())

def add_product():
    new_product = str(input("Enter new product:"))
    products.append(new_product)
    print("\n", products)
    return(product_menu())

#Create an f string and use {} in place of "list_name"

def add_courier():
    new_courier = str(input("Enter new courier:"))
    couriers.append(new_courier)
    print("\n", couriers)
    return(courier_menu())

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

def update_courier():
    print("\nChoose item to update:")
    print("[0] Return to courier Menu")
    for courier in couriers:
        print(f"[{couriers.index(courier) + 1}] {courier}")
    options = (int(input("Enter number here: ")) - 1)
    if options == -1:
        return(courier_menu())
    elif (options - 1) >= 0 and (options) < len(couriers):
        print(f"You have chosen: {couriers[options]}")
        updated_courier = str(input("Enter updated courier: "))
        couriers[options] = updated_courier
        return(courier_menu())
    else:
        print("\nEntry Error: Please try again")
        return(update_courier())

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

def delete_courier():
    print("\nChoose item to delete:")
    print("[0] Return to courier Menu")
    for courier in couriers:
        print(f"[{couriers.index(courier) + 1}] {courier}")
    options = (int(input("Enter number here: ")) - 1)
    if options == -1:
        return(courier_menu())
    elif (options - 1) >= 0 and (options) < len(couriers):
        print(f"You have chosen: {couriers[options]}. Are you sure you want to continue?")
        confirmation_dialogue = str(input("[Y] for yes, [N] for no: "))
        if confirmation_dialogue == "Y" or confirmation_dialogue == "y":
            print(f"You have deleted {couriers[options]}")
            couriers.remove(couriers[options])
            return(courier_menu())
        elif confirmation_dialogue == "N" or confirmation_dialogue == "n":
            return(courier_menu())
        else:
            print("\nEntry Error: Returning to courier Menu")
            return(courier_menu())
    else:
        print("\nEntry Error: Please try again")
        return(courier_menu())

products = []
couriers = []


import_products()
import_couriers()
main_menu()
try:
    with open('products.txt', 'w') as file:
        contents = file.read()
        print(contents)
except:
    