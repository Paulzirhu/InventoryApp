from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country 
        self.code = code 
        self.product = product  
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        return self.cost
        
    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file) 
            for line in file:
                temp = line.strip().split(", ")
                if len(temp) == 5:
                    shoe_list.append(Shoe(temp[0], temp[1], temp[2], float(temp[3]), int(temp[4])))
                else:
                    print("Invalid data format in inventory file:", line)
        print("Data successfully loaded from inventory.txt.")
    except FileNotFoundError:
        print("Error: Inventory file not found.")
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


def capture_shoes():
    """
    Capture data about a new shoe from the user and add it to the shoe list.

    This function prompts the user to enter details of a new shoe,
    validates the input, creates a Shoe object, and adds it to the shoe_list.

    Raises:
        ValueError: If user input is invalid.
        Exception: For any other unexpected errors.
    """
    try:
        country = input("Please enter country: ")
        code = input("Please enter code: ")
        product = input("Please enter product: ")
        cost = float(input("Please enter cost: "))
        if cost < 0:
            raise ValueError("Cost cannot be negative.")
        quantity = int(input("Please enter quantity: "))
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        shoe_list.append(Shoe(country, code, product, cost, quantity))
        print("Shoe data captured successfully.")
    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    rows = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
    print(tabulate(rows, headers=headers))

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    min_quantity_shoe = min(shoe_list, key=lambda x: x.quantity)
    print("Shoe with lowest quantity:", min_quantity_shoe)
    restock_qty = int(input("How many shoes do you want to restock? "))
    min_quantity_shoe.quantity += restock_qty
    print("Restocked successfully.")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code = input("Please enter shoe code to search: ")
    found = False
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            found = True
            break
    if not found:
        print("Shoe not found.")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"The total value for {shoe.product} is {value}")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    max_quantity_shoe = max(shoe_list, key=lambda x: x.quantity)
    print("Product with highest quantity:", max_quantity_shoe.product, "is for sale.")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    print("\n========== Main Menu ==========")
    print("1. Read shoes data from file")
    print("2. Capture new shoe data")
    print("3. View all shoes")
    print("4. Re-stock shoes")
    print("5. Search for a shoe")
    print("6. Calculate value per item")
    print("7. Find product with highest quantity")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        read_shoes_data()
    elif choice == '2':
        capture_shoes()
    elif choice == '3':
        view_all()
    elif choice == '4':
        re_stock()
    elif choice == '5':
        search_shoe()
    elif choice == '6':
        value_per_item()
    elif choice == '7':
        highest_qty()
    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
