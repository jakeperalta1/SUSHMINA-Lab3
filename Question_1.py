print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1.Add the product to the cart.")
print("2.Search the product.")
print("3.Delete the product from the cart.")
print("4.Quit.")

shoppingCart={}

while True:
    x=int(input("Enter your choice: "))
    if x==1:
        ee= int(input("Enter the number of items to be added in the cart: "))
        for i in range(ee):
            if len(shoppingCart)==5:
                 print("Inventory is full.")
            
            
            product_name=input("Enter item: ")
            brand=input("Enter brand name:")
            shoppingCart.update({product_name:brand})
            print(shoppingCart)
        print("You entered following items in the cart.")