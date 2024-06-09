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
    cls()
    print("Done!")
    time.sleep(0.5)
    cls()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def get_all_stock_information():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation')
    TechStoreStockInformation = cursor.fetchall()\
    

    for product in TechStoreStockInformation:
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")


def get_all_stock_information_by_ascending_retail_price():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY RetailPrice ASC"
    cursor.execute(query)
    get_all_stock_information_by_ascending_retail_price = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_ascending_retail_price):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_descending_retail_price():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY RetailPrice DESC"
    cursor.execute(query)
    get_all_stock_information_by_descending_retail_price = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_descending_retail_price):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_ascending_manufacturing_cost():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY ManufacturingCost ASC"
    cursor.execute(query)
    get_all_stock_information_by_ascending_manufacturing_cost = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_ascending_manufacturing_cost):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_descending_manufacturing_cost():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY ManufacturingCost DESC"
    cursor.execute(query)
    get_all_stock_information_by_descending_manufacturing_cost = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_descending_manufacturing_cost):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_ascending_weight():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY Weight ACS"
    cursor.execute(query)
    get_all_stock_information_by_descending_weight = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_descending_weight):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_descending_weight():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY Weight DESC"
    cursor.execute(query)
    get_all_stock_information_by_descending_weight = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_descending_weight):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_ascending_stock():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY Stock ASC"
    cursor.execute(query)
    get_all_stock_information_by_ascending_stock = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_ascending_stock):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_descending_stock():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY Stock DESC"
    cursor.execute(query)
    get_all_stock_information_by_descending_stock = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_descending_stock):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def add_product():
    ProductID = input(int("Enter product ID: "))
    Name = input("Enter product name: ")
    RetailPrice = int(input("Enter product retail price: "))
    ManufacturingCost = int(input("Enter product manufacturing cost: "))
    Weight = int(input("Enter product weight: "))
    Stock = int(input("Enter product number of stock: "))

    query = "INSERT INTO TechStoreStockInformation (Country, population_in_1980, population_in_2022) VALUES (?, ?, ?)"
    cursor.execute(query, (ProductID, Name, RetailPrice, ManufacturingCost, Weight, Stock))
    conn.commit()
    print("Product added successfully!")

def delete_product():
    get_all_stock_information()
    choice = int(input("Enter the ID of the product you want to delete: "))
    cursor.execute("SELECT * FROM TechStoreStockInformation")
    TechStoreStockInformation = cursor.fetchall()
    if choice <= len(TechStoreStockInformation) and choice > 0:
        ProductID = TechStoreStockInformation[choice - 1][0] #[choice - 1] is the user choice, [0] assumes ID is first col
        cursor.execute("DELETE FROM TechStoreStockInformation WHERE id=?", (ProductID,))
        conn.commit()
        print("Product deleted successfully!")
    else:
        print("Invalid choice")

def edit_product():
    get_all_stock_information()
    choice = int(input("Enter the ID of the product you want to edit: "))
    cursor.execute("SELECT * FROM TechStoreStockInformation")
    TechStoreStockInformation = cursor.fetchall()
    if choice <= len(TechStoreStockInformation) and choice > 0:
        ProductID = TechStoreStockInformation[choice - 1][0]  
        print("1. Product_name\n2. RetailPrice\n3. ManufacturingCost\n4. Weight\n5. Stock")
        edit_choice = int(input("Enter the number of the attribute you want to edit: "))
        if edit_choice == 1:
            new_name = input("Enter product's new name: ")
            cursor.execute("UPDATE TechStoreStockInformation SET Name=? WHERE id=?", (new_name, ProductID))
            conn.commit()
            print("Product name updated successfully!")

        elif edit_choice == 2:
            RetailPrice = float(input("Enter new retail price: "))
            cursor.execute("UPDATE TechStoreStockInformation SET RetailPrice=? WHERE id=?", (RetailPrice, ProductID))
            conn.commit()
            print("Product price updated successfully!")

        elif edit_choice == 3:
            ManufacturingCost = float(input("Enter new manufacturing cost: "))
            cursor.execute("UPDATE TechStoreStockInformation SET ManufacturingCost=? WHERE id=?", (ManufacturingCost, ProductID))
            conn.commit()
            print("Product manufacturing cost updated successfully!")

        elif edit_choice == 4:
            Weight = float(input("Enter new weight: "))
            cursor.execute("UPDATE TechStoreStockInformation SET Weight=? WHERE id=?", (Weight, ProductID))
            conn.commit()
            print("Product weight updated successfully!")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")


while True:
    while True:
        cls()
        user_menu()
        print("Type the NUMBER of the query you want to run below:")
        user_input = input("> ")
        if user_input == "1":
            get_all_stock_information()
            break
        if user_input == "2":
            get_all_stock_information_by_ascending_retail_price()
            break
        if user_input == "3":
            get_all_stock_information_by_descending_retail_price()
            break
        if user_input == "4":
            get_all_stock_information_by_ascending_manufacturing_cost()
            break
        if user_input == "5":
            get_all_stock_information_by_descending_manufacturing_cost()
            break
        if user_input == "6":
            get_all_stock_information_by_ascending_weight()
            break
        if user_input == "7":
            get_all_stock_information_by_descending_weight()
        if user_input == "8":
            get_all_stock_information_by_ascending_stock()
        if user_input == "9":
            get_all_stock_information_by_descending_stock()
        if user_input == "10":
            add_product()
        if user_input == "11":
            delete_product()
        if user_input == "12":
            edit_product()   
        else:
            print("Error, please type a number.")
            time.sleep(3)

    print("Press ENTER to show options menu")
    user_confirmation = input("> ")
    loading()
    