print("===Customer Behaviour Dataset Anaylizer===")
print("1: Add Customer Record")
print("2: View All Record")
print("3: Search Customer")
print("4: Anaylize Purchases")
import json 
def add_customer_record():
    print("Hi! Add Customer Record")
     #customer id  
    customer_id = input("Enter Customer Name as Id: ").strip()
    if not customer_id.isalpha():
        print("Invalid Id! Example: ali")
        return     
    
    age = int(input("Enter your age: ").strip())
    if age<10:
        print("Invalid Age! Example: 22")
        if age>= 10:
            print("Age is Valid")
            return 
    product = input("Which product is purchased: ").strip() 
    if not product.isalnum():
        print("Invalid Product! Example Food, Dress, shoes etc")
        return 
    amount = int(input("Enter your amount = ")) 

    try:
     with open("Add Customer Record.json","r") as file:
       customer = json.load(file)
    except FileNotFoundError:
     customer = []
    customers = {
            "Customer Id": customer_id,
            "Age": age,
            "Product": product,
            "Amount": amount,
           }   
    customer.append(customers)
    with open("Add Customer Record.json","w") as file:
       json.dump(customer,file,indent=4)
    print("Successfully Saved")


def view_all_record():
    def view_all_record():
     print("View All Customers")

    try:
        with open("Add Customer Record.json", "r") as file:
            customers = json.load(file)

    except FileNotFoundError:
        print("File not found")
        return

    if not customers:
        print("No customer records found")
        return

    for customer in customers:
        print("Customer ID:", customer["Customer Id"])
        print("Age:", customer["Age"])
        print("Product:", customer["Product"])
        print("Amount:", customer["Amount"])
        print("--------------------")
def search_customer():
  
    search_id = input("Enter Customer ID: ").strip()

    try:
        with open("Add Customer Record.json", "r") as file:
            customers = json.load(file)

    except FileNotFoundError:
        print("File not found")
        return

    for customer in customers:
        if search_id == customer["Customer Id"]:
            print("Customer Record Found")
            print(customer)
            return

    print("Customer not found")

   
def analyze_purchases():
    print("=== Purchase Analysis ===")

    try:
        with open("Add Customer Record.json", "r") as file:
            customers = json.load(file)

    except FileNotFoundError:
        print("File not found")
        return

    if not customers:
        print("No customer records found")
        return

    total_purchase = 0

    for customer in customers:
        total_purchase += customer["Amount"]

    average_purchase = total_purchase / len(customers)

    print("Total Purchase:", total_purchase)
    print("Average Purchase:", round(average_purchase, 2))



while True:
   choice = int(input("Enter your choice = "))
   if choice == 1:
      print(add_customer_record())
   elif choice == 2:
      print(view_all_record())
   elif choice == 3:
      print(search_customer())
   elif choice == 4:
      print(analyze_purchases())
   else:
      print("Invalid Choice!")