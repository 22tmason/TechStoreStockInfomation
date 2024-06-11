import sqlite3
import time
import os

conn = sqlite3.connect("TechStoreStockInformation.db")
cursor = conn.cursor()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
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


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
    print()

def get_all_stock_information_by_product_id_ascending():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY ProductID ASC')
    TechStoreStockInformation = cursor.fetchall()\
   
    for product in TechStoreStockInformation:
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_product_id_descending():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation ORDER BY ProductID DESC')
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

    for product in get_all_stock_information_by_ascending_retail_price:
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

    for product in get_all_stock_information_by_descending_retail_price:
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

    for product in get_all_stock_information_by_ascending_manufacturing_cost:
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

    for product in get_all_stock_information_by_descending_manufacturing_cost:
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

    for product in get_all_stock_information_by_descending_weight:
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

    for product in get_all_stock_information_by_descending_weight:
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

    for product in get_all_stock_information_by_ascending_stock:
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

    for product in get_all_stock_information_by_descending_stock:
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

while True:
    while True:
        cls()
        user_menu()
        print("Type the NUMBER of the query you want to run below:")
        user_input = input("> ")
        if user_input == "1":
            get_all_stock_information_by_product_id_ascending()
            break
        if user_input == "2":
            get_all_stock_information_by_product_id_descending()
            break
        if user_input == "3":
            get_all_stock_information_by_ascending_retail_price()
            break
        if user_input == "4":
            get_all_stock_information_by_descending_retail_price()
            break
        if user_input == "5":
            get_all_stock_information_by_ascending_manufacturing_cost()
            break
        if user_input == "6":
            get_all_stock_information_by_descending_manufacturing_cost()
            break
        if user_input == "7":
            get_all_stock_information_by_ascending_weight()
            break
        if user_input == "8":
            get_all_stock_information_by_descending_weight()
        if user_input == "9":
            get_all_stock_information_by_ascending_stock()
        if user_input == "10":
            get_all_stock_information_by_descending_stock()  
        else:
            print("Error, please type a number.")
            time.sleep(3)

    print("Press ENTER to show options menu")
    user_confirmation = input("> ")
    loading()
    