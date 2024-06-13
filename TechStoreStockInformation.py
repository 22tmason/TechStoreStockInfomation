import sqlite3
import time
import os
from prettytable import PrettyTable

conn = sqlite3.connect("TechStoreStockInformation.db")
cursor = conn.cursor()

def loading():
    cls()
    time.sleep(0.25)
    print("Loading")
    time.sleep(0.25)
    cls()
    print("Loading.")
    time.sleep(0.25)
    cls()
    print("Loading..")
    time.sleep(0.25)
    cls()
    print("Loading...")
    time.sleep(0.25)
    cls()
    print("Done!")
    time.sleep(0.5)
    cls()
# defines clear, so the terimal can be clared, keeping the terminal clean.
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# defines the user menu
def user_menu():
    print("Options Menu:")
    print()
    print("1.   Get all product information, sort by product ID ascending")
    print("2.   Get all product information, sort by product ID descending")
    print("3.   Get all product information, sort by retail price ascending")
    print("4.   Get all product information, sort by retail price descending")
    print("5.   Get all product information, sort by manufacturing cost ascending")
    print("6.   Get all product information, sort by manufacturing cost descending")
    print("7.   Get all product information, sort by weight ascending")
    print("8.   Get all product information, sort by weight descending")
    print("9.   Get all product information, sort by number of stock ascending")
    print("10.  Get all product information, sort by number of stock descending")
    print("11.  Get all warranty periods")
    print("12.  Add product")
    print("13.  Delete product")
    print("14.  Edit product")
    print("15.  Calculate profit margins")
    print()
# defines gets all stock product ID ascending.
def get_all_stock_information_by_product_id_ascending():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY ProductID ASC')
    TechStoreStockInformation = cursor.fetchall()
    # Creates a PrettyTable to make it look nice.
    table = PrettyTable()
    # Gets the column names from the cursor description
    column_names = [desc[0] for desc in cursor.description]
    # This adds headers to the table for each column
    table.field_names = column_names
    # Add rows to the table from the database.
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)
# defines gets all stock product ID descending
def get_all_stock_information_by_product_id_descending():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY ProductID DESC')
    TechStoreStockInformation = cursor.fetchall()
   
    table = PrettyTable()
    column_names = [desc[0] for desc in cursor.description]
    table.field_names = column_names
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)

def get_all_stock_information_by_ascending_retail_price():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY RetailPrice ASC')
    TechStoreStockInformation = cursor.fetchall()
    
    table = PrettyTable()
    column_names = [desc[0] for desc in cursor.description]
    table.field_names = column_names
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)

def get_all_stock_information_by_descending_retail_price():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY RetailPrice DESC')
    TechStoreStockInformation = cursor.fetchall()

    table = PrettyTable()
    column_names = [desc[0] for desc in cursor.description]
    table.field_names = column_names
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)

def get_all_stock_information_by_ascending_manufacturing_cost():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY ManufacturingCost ASC')
    TechStoreStockInformation = cursor.fetchall()

    table = PrettyTable()
    column_names = [desc[0] for desc in cursor.description]
    table.field_names = column_names
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)

def get_all_stock_information_by_descending_manufacturing_cost():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY ManufacturingCost DESC')
    TechStoreStockInformation = cursor.fetchall()

    table = PrettyTable()
    column_names = [desc[0] for desc in cursor.description]
    table.field_names = column_names
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)

def get_all_stock_information_by_ascending_weight():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY Weight ASC')
    TechStoreStockInformation = cursor.fetchall()

    table = PrettyTable()
    column_names = [desc[0] for desc in cursor.description]
    table.field_names = column_names
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)

def get_all_stock_information_by_descending_weight():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY Weight DESC')
    TechStoreStockInformation = cursor.fetchall()

    table = PrettyTable()
    column_names = [desc[0] for desc in cursor.description]
    table.field_names = column_names
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)

def get_all_stock_information_by_ascending_stock():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY Stock ASC')
    TechStoreStockInformation = cursor.fetchall()

    table = PrettyTable()
    column_names = [desc[0] for desc in cursor.description]
    table.field_names = column_names
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)

def get_all_stock_information_by_descending_stock():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY Stock DESC')
    TechStoreStockInformation = cursor.fetchall()

    table = PrettyTable()
    column_names = [desc[0] for desc in cursor.description]
    table.field_names = column_names
    for product in TechStoreStockInformation:
        table.add_row([
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5]
        ])
    print(table)
# defines adding a product.
def get_all_warranty_periods():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformationSecondaryTable')
    TechStoreStockInformationSecondaryTable = cursor.fetchall()
    table = PrettyTable()
    # Gets the column names from the cursor description
    column_names = [desc[0] for desc in cursor.description]
    # This adds headers to the table for each column
    table.field_names = column_names
    # Add rows to the table from the database.
    for product in TechStoreStockInformationSecondaryTable:
        table.add_row([
            product[0],
        ])
    print(table)

def add_product():
    loading()
    # bthe six statements below get the user to enter the product information of the new product.
    ProductID = int(input("Enter product ID: "))
    Name = input("Enter product name: ")
    RetailPrice = int(input("Enter product retail price: "))
    ManufacturingCost = int(input("Enter product manufacturing cost: "))
    Weight = int(input("Enter product weight: "))
    Stock = int(input("Enter product's number of stock: "))
    # adds the new product into the database
    query = "INSERT INTO TechStoreStockInformation (ProductID, Name, RetailPrice, ManufacturingCost, Weight, Stock) VALUES (?, ?, ?, ?, ?, ?)"
    # to make the program more robust, I added a try and except to make sure the program doesn't crash.
    try:
        # excutes the query with the new product details included.
        cursor.execute(query, (ProductID, Name, RetailPrice, ManufacturingCost, Weight, Stock))
        # saves the changes made.
        conn.commit() 
        print("Product added successfully!") # lets the user know that the process was successful.
    except sqlite3.Error as error_message:
        # if anything goes wrong, it will print an error message to let the user know that the adding of the product was unsuccessful.
        print(f"Error adding product: {error_message}")

def delete_product():
    get_all_stock_information_by_product_id_ascending() # helps the user know what product they want to delete.
    print("")
    # asks the user for the ID of the product that will be deleted.
    ProductID = input("Enter product ID to delete: ")
    # excutes the query to delete the product with the productID
    # This will make sure that the ProductID is passed as a tuple (with a comma after ProductID)
    cursor.execute("DELETE FROM TechStoreStockInformation WHERE ProductID=?", (ProductID,))
    # saves the changes made.
    conn.commit()
    # lets the user know that the process was successful.
    print(f"Product with ProductID '{ProductID}' deleted successfully!")

def edit_product():
    # helps the user know what product they want to delete.
    get_all_stock_information_by_product_id_ascending()
    # gets the user to choice the ID of the product that they want to edit.
    choice = int(input("Enter the ID of the product you want to edit: "))
    # gets all the stock inforamtion
    cursor.execute("SELECT * FROM TechStoreStockInformation")
    TechStoreStockInformation = cursor.fetchall()
    # to make sure the program doesn't break, this checks if the users choice makes sense.
    if choice <= len(TechStoreStockInformation) and choice > 0:
        ProductID = TechStoreStockInformation[choice - 1][0]  
        print("1. Name\n2. RetailPrice\n3. ManufacturingCost\n4. Weight\n5. Stock")
        edit_choice = int(input("Enter the number of the attribute you want to edit: "))
        # the different appributes of the product that can be edited.	
        if edit_choice == 1:
            new_name = input("Enter product's new name: ")
            cursor.execute("UPDATE TechStoreStockInformation SET Name=? WHERE ProductID=?", (new_name, ProductID))
            conn.commit()
            print("Product name updated successfully!")

        elif edit_choice == 2:
            RetailPrice = float(input("Enter new retail price: "))
            cursor.execute("UPDATE TechStoreStockInformation SET RetailPrice=? WHERE ProductID=?", (RetailPrice, ProductID))
            conn.commit()
            print("Product price updated successfully!")

        elif edit_choice == 3:
            ManufacturingCost = float(input("Enter new manufacturing cost: "))
            cursor.execute("UPDATE TechStoreStockInformation SET ManufacturingCost=? WHERE ProductID=?", (ManufacturingCost, ProductID))
            conn.commit()
            print("Product manufacturing cost updated successfully!")

        elif edit_choice == 4:
            Weight = float(input("Enter new weight (): "))
            cursor.execute("UPDATE TechStoreStockInformation SET Weight=? WHERE ProductID=?", (Weight, ProductID))
            conn.commit()
            print("Product weight updated successfully!")
            # 
        elif edit_choice == 5:
            Stock = int(input("Enter new weight (grams): "))
            cursor.execute("UPDATE TechStoreStockInformation SET Stock=? WHERE ProductID=?", (Stock, ProductID))
            conn.commit()
            # lets the user know that the process was successful
            print("Product stock updated successfully!")
        else:
            # lets the user know that the process was unsuccessful
            print("Invalid choice")
    else:
        # lets the user know that the process was unsuccessful
        print("Invalid choice")

def calculate_profit_margin():
    try:
        # This gets the data from the database in SQLite
        cursor.execute("SELECT ProductID, Name, RetailPrice, ManufacturingCost, Weight, Stock FROM TechStoreStockInformation")
        products = cursor.fetchall()
        
        if not products:
            print("No products found in the database.")
            return
        
        # Create a PrettyTable instance to make it look nice.
        table = PrettyTable()
        
        # This defines the column names and adds them to the table
        column_names = ["ProductID", "Name", "RetailPrice", "ManufacturingCost", "Weight", "Stock", "Profit Margin (%)"]
        table.field_names = column_names
        
        # For loop to go over the products and add rows to the table
        for product in products:
            ProductID, Name, RetailPrice, ManufacturingCost, Weight, Stock = product
            
            # How the profit margins of all of the products are calculated.
            if RetailPrice > 0:
                profit_margin = ((RetailPrice - ManufacturingCost) / RetailPrice) * 100
            else:
                profit_margin = 0
            
            # Table.add_row adds the data to the rows, which are in the brakets.
            table.add_row([ProductID, Name, RetailPrice, ManufacturingCost, Weight, Stock, f"{profit_margin:.2f}%"])
        
        # This statement prints the table
        print(table)
        
    except sqlite3.Error as e:
        print(f"Error retrieving products: {e}")

# the passwords for the user to access the database
correct_password = "strongpassword34"
max_attempts = 3

print("TECH STORE STOCK INFORMATION")
print("")
while max_attempts > 0:
    print("Enter password for access to database:")
    entered_password = input("> ")
    if entered_password == correct_password:            
        print("Access granted!")
        time.sleep(3)
        while True:
            while True:
                cls()
                user_menu()
                print("Type the NUMBER of the query you want to run below:")
                user_input = input("> ")
                # the following below are how the users input is turned into a query to be run.
                if user_input == "1":
                    get_all_stock_information_by_product_id_ascending()
                    break
                elif user_input == "2":
                    get_all_stock_information_by_product_id_descending()
                    break
                elif user_input == "3":
                    get_all_stock_information_by_ascending_retail_price()
                    break
                elif user_input == "4":
                    get_all_stock_information_by_descending_retail_price()
                    break
                elif user_input == "5":
                    get_all_stock_information_by_ascending_manufacturing_cost()
                    break
                elif user_input == "6":
                    get_all_stock_information_by_descending_manufacturing_cost()
                    break
                elif user_input == "7":
                    get_all_stock_information_by_ascending_weight()
                    break
                elif user_input == "8":
                    get_all_stock_information_by_descending_weight()
                    break
                elif user_input == "9":
                    get_all_stock_information_by_ascending_stock()
                    break
                elif user_input == "10":
                    get_all_stock_information_by_descending_stock()  
                    break
                elif user_input == "11":
                    get_all_warranty_periods()
                    break
                elif user_input == "12":
                    add_product()
                    break
                elif user_input == "13":
                    delete_product()
                    break
                elif user_input == "14":
                    edit_product()
                    break
                elif user_input == "15":
                    calculate_profit_margin()
                    break
                else:
                    print("Error, please type a number.")
                    time.sleep(3)
                    cls()

            print("Press ENTER to show options menu")
            user_confirmation = input("> ")
            loading()
    else:
        max_attempts = max_attempts - 1
        # lets the user know that got the password incorrect and have ? attempts left.
        print(f"Incorrect password. You have {max_attempts} attempts left.")

# end of program, the user failed to enter the correct password.
print("Access denied. Too many incorrect attempts.")