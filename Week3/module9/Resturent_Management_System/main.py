from fooditem import FoodItem
from menu import Menu
from user import Customer, Admin, Employee
from restaurent import Restaurent
from order import Order


mama = Restaurent("MAMA Restaurent")

def customer_menu():
    name = input("Enter your name : ")
    email = input("Enter your Email : ")
    phone = input("Enter your Phone : ")
    address = input("Enter your Address : ")
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice =  int(input("Enter Your choice : "))

        if choice == 1:
            customer.view_menu(restaurent=mama)
        elif choice == 2:
            item_name = input("Enter item name : ")
            quantity = int(input("Enter item quantity : "))
            customer.add_to_cart(restaurent=mama, item_name=item_name, quantity=quantity)
        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid input")


def admin_menu():
    name = input("Enter your name : ")
    email = input("Enter your Email : ")
    phone = input("Enter your Phone : ")
    address = input("Enter your Address : ")
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {admin.name}")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View Employee")
        print("4. View items")
        print("5. Delete items")
        print("6. Exit")

        choice =  int(input("Enter Your choice : "))

        if choice == 1:
            item_name = input("Enter item name : ")
            item_price = int(input("Enter item price : "))
            item_quantity = int(input("Enter item quantitiy"))
            item = FoodItem(name=item_name, price=item_price, quantity=item_quantity)
            admin.add_new_item(restaurent=mama, item=item)
        elif choice == 2:
            # name, phone, email, address, age, designation, salary
            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            address = input("Enter employee address : ")
            age = input("Enter employee age : ")
            designation = input("Enter employee designation : ")
            salary = input("Enter employee salary : ")
            employee = Employee(name=name, phone=phone, email=email, address=address, 
                                age=age, designation=designation, salary=salary)
            admin.add_employee(restaurent=mama, employee=employee)
        elif choice == 3:
            admin.view_employee(restaurent=mama)
        elif choice == 4:
            admin.view_menu_item(restaurent=mama)
        elif choice == 5:
            admin.remove_item(restaurent=mama, item=item)
        elif choice == 6:
            break
        else:
            print("Invalid Input")


while True:
    print(f"Welcome to {mama.name}")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input")
         
        