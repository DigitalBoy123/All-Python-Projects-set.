menu= {
    "pizza": 2100,
    "pasta": 8600,
    "salad": 1000,
    "tea": 500,
    "coffee": 600,
    "juice": 700,
    "soda": 800,
    "water": 300,
    "milk": 400,
    "dessert": 1200,
    "soup": 950,
}

print("Welcome to the Restaurant Menu!")
print("Menu:")
print("*"*135)
print("Here is the list of items we have:")
for item, price in menu.items():
    print(f"{item}: {price} Rs")
print("*"*135)
total_price = 0
while True:
        order = input("Enter your order: ").lower()
        if order in menu:
            total_price += menu[order]
            print(f"Your {order} has been ordered!")
            break
        else:
            print("Your order is not in our menu! Please choose something else!")
            
while True:
    choice = input("Do you wanna order something else? ").lower()
    if choice == "yes":
        reorder = input("Enter something: ").lower()
        try:
            total_price += menu[reorder]
            print(f"Your {reorder} has been ordered!")
        except KeyError:
            print(("Your order is not in our menu! Please choose something else!"))
    elif choice == "no":
        print("If you need anything for the next time then just order!!")
        break
    else:
        print("Invalide choice for yes/no")
        
print(f"The total prize is: {total_price}")
print("*"*135)
print("Thanks for ordering items from our Restaurant!!")


 
            

    