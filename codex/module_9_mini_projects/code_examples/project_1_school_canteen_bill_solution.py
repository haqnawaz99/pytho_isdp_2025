def calculate_total(price, quantity):
    return price * quantity

item_name = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = calculate_total(price, quantity)
print(f"{item_name} total bill: {total}")
