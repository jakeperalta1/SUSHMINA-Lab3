print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1.Add the product to the cart.")
print("2.Search the product.")
print("3.Delete the product from the cart.")
print("4.Quit.")

#making an empty list
shoppingCart={}

#creating a loop to proceed with different options.
while True:
    x=int(input("Enter your choice: "))
    if x==1:
        ee= int(input("Enter the number of items to be added in the cart: "))
        
        #limiting items to be entered
        for i in range(ee):
                if len(shoppingCart)==5:
                 print("Cart is full.")
                 break
            
                 #entering products
                product_name=input("Enter item:")
                brand=input("Enter brand name:")
                shoppingCart.update({product_name:brand})
                print(shoppingCart)
                print("You entered following items in the cart.")
    
    
    
    elif x==2:
            #searching items
             f= input("Enter the item to be searched:")
             if f in shoppingCart:
                print({product_name:brand})
             else:
                 print("No product exist with this name.")
            
    elif x==3:
            #deleting items
            g= input("Enter item to delete:")
            del shoppingCart[g]
            print("item deleted")
            if shoppingCart == {}:
                print("Cart is empty, no item is found")
    
    elif x==4:
        #exiting from system
        print("Exited.")
        break
        
    else:
        print("Wrong option entered.")
        



            
    
    
    
