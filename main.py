import json
import os


def welcome():
    """ Welcome Screen """
    os.system('cls')
    print("\n\n\t\t\t\t\t\t\tWelcome to\n\n\t\t\t\t\t\tInventory Management System")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress 'Enter' key to continue...", end='')
    input()


def modify():
    """ modify method """
    fin = open('file.json', 'r')
    data = fin.read()
    fin.close()
    jsn = json.loads(data)

    os.system('cls')
    print("\n\t\t\t\t\t\t\tMODIFY PRODUCT")

    print("\n\n\nEnter the product id you want to modify: ", end='')
    id = input()
    r_data = jsn[id]
    print(F"\n\tThe name of the product is {r_data[0]}")
    print(F"\tIts price is {r_data[1]}")
    print(F"\tThe quantity we have is {r_data[2]}")
    print(F"\tThe GST charge (18%) is {r_data[3]}")
    print(F"\tIt was purchased on {r_data[4]}\n")

    print("\nWhat do you want to modify:")
    print("\t1. Price\n\t2. Quantity\n\t3. GST charge\n\t4. Time of purchase")
    print("\nHERE: ", end='')
    index = int(input())

    print(F"\nThe data you want to modify is {r_data[index]}")
    print("Enter new value: ", end='')
    new_value = input()
    r_data[index] = new_value
    jsn[id] = r_data

    data = json.dumps(jsn)
    fout = open('file.json', 'w')
    fout.write(data)
    fout.close()

    print("\n\n\n\t\t\tDATA SUCCESSFULLY MODIFIED!!!")
    print("\n\n\n\n\nPress 'Enter' key to continue...", end='')
    input()


def search():
    """Search method"""
    fin = open('file.json', 'r')
    data = fin.read()
    fin.close()
    jsn = json.loads(data)

    os.system('cls')
    print("\n\t\t\t\t\t\t\tSEARCH PRODUCT")

    print("\n\n\nEnter the product id you want to search for: ", end='')
    id = input()
    r_data = jsn[id]
    print(F"\n\tThe name of the product is {r_data[0]}")
    print(F"\tIts price is {r_data[1]}")
    print(F"\tThe quantity we have is {r_data[2]}")
    print(F"\tThe GST charge (18%) is {r_data[3]}")
    print(F"\tIt was purchased on {r_data[4]}\n")

    print("\n\n\n\n\nPress 'Enter' key to continue...", end='')
    input()


def showAll():
    """A method to show all products"""
    fin = open('file.json', 'r')
    data = fin.read()
    fin.close()
    jsn = json.loads(data)

    os.system('cls')
    print("\n\t\t\t\t\t\t\tSHOW ALL PRODUCT")
    print("\n\n\nProduct ID----Name----Price----Quantity----GST Charge----Time of Purchase")
    for key in jsn.keys():
        print(F"{key}------{jsn[key][0]}----{jsn[key][1]}----{jsn[key][2]}----{jsn[key][3]}----{jsn[key][4]}")

    print("\n\n\n\n\nPress 'Enter' key to continue...", end='')
    input()


def addNew():
    """A method to add new products into the inventory"""
    fin = open('file.json', 'r')
    data = fin.read()
    fin.close()
    jsn = json.loads(data)

    os.system('cls')
    print("\n\t\t\t\t\t\t\tADD NEW PRODUCT")
    print("\n\n\nEnter the new product ID: ", end='')
    new_id = input()
    print("Enter new product name: ", end='')
    new_name = input()
    print("Enter new product price: ", end='')
    new_price = input()
    print("Enter new product quantity: ", end='')
    new_quantity = input()
    print("Enter new product GST charge: ", end='')
    new_GST = input()
    print("Enter new product time of purchase: ", end='')
    new_time = input()

    print("\n\nThe details of the new product is as follows: ")
    print(F"\tThe product ID is {new_id}")
    print(F"\tThe name of the product is {new_name}")
    print(F"\tIts price is {new_price}")
    print(F"\tThe quantity we have is {new_quantity}")
    print(F"\tThe GST charge (18%) is {new_GST}")
    print(F"\tIt was purchased on {new_time}\n")

    list = []
    list.append(new_name)
    list.append(new_price)
    list.append(new_quantity)
    list.append(new_GST)
    list.append(new_time)
    jsn[new_id] = list

    data = json.dumps(jsn)
    fout = open('file.json', 'w')
    fout.write(data)
    fout.close()

    print("\n\n\n\t\t\tDATA SUCCESSFULLY ADDED INTO INVENTORY!!!")
    print("\n\n\n\n\nPress 'Enter' key to continue...", end='')
    input()


def delProd():
    """A method to delete product from inventory"""
    fin = open('file.json', 'r')
    data = fin.read()
    fin.close()
    jsn = json.loads(data)

    os.system('cls')
    print("\n\t\t\t\t\t\t\tDELETE PRODUCT")

    print("\n\n\nEnter product ID which you wish to delete: ", end='')
    id = input()
    r_data = jsn[id]
    print(F"\n\tThe name of the product is {r_data[0]}")
    print(F"\tIts price is {r_data[1]}")
    print(F"\tThe quantity we have is {r_data[2]}")
    print(F"\tThe GST charge (18%) is {r_data[3]}")
    print(F"\tIt was purchased on {r_data[4]}\n")
    jsn.pop(id)

    data = json.dumps(jsn)
    fout = open('file.json', 'w')
    fout.write(data)
    fout.close()

    print("\n\n\n\t\t\tDATA SUCCESSFULLY DELETED FROM INVENTORY!!!")
    print("\n\n\n\n\nPress 'Enter' key to continue...", end='')
    input()

def menu():
    """ menu method """
    os.system('cls')
    print("\n\t\t\t\t\t\t\tMENU")
    print("\n\n\nEnter your choice:")
    print("\t1. Modify product")
    print("\t2. Search product")
    print("\t3. Show all products")
    print("\t4. Add new product")
    print("\t5. Delete product")
    print("\nHERE: ", end='')
    choice = int(input())
    if choice == 1:
        modify()
    elif choice == 2:
        search()
    elif choice == 3:
        showAll()
    elif choice == 4:
        addNew()
    elif choice == 5:
        delProd()
    else:
        menu()

if __name__ == '__main__':
    welcome()
    while True:
        menu()
