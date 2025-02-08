menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':40,
}
print("Welcome to Python Restaurant")
print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 40")
order_total = 0
while True:
 item_1=input("Enter the name of item you want to order = ").capitalize()
 if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

 else:
    print(f"Ordered item {item_1} is not available yet!")

 another_order=input("Do you want to add another item? (Yes/No)").capitalize()
 if another_order=="No":
    break
print(f"The total amount of items to pay is {order_total}")
print("THANK YOU!!")
            
