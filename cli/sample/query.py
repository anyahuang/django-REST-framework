#!/usr/bin/env python3
from data import stock

user_name = input("Enter you name: ",)
print("Good morning",user_name)

num = input("Please select : \n1. List items by warehouse, \n2. Search an item and place an order\n3. Quit.\n ")

if num == "1" :
   for item1 in warehouse1:
     print("-",item1)
   for item2 in warehouse2:
      print("-",item2)     
elif num == "2" :
     item_name = input("Please input the item name :") 
     #w1=the item which user selected -how many in wearhouse1
     w1=warehouse1.count(item_name)
     w2=warehouse2.count(item_name)
     if warehouse1.count(item_name)> 0 and warehouse2.count(item_name)>0:
        print("Both warehouses")
     elif w1>w2:
        print("Warehouse 1 has higher amount of item and it has ",w1,"item(s)") 
     elif w1< w2:
        print("Warehouse 2 has higher amount of item ","it has",w2,"item(s)")
     elif warehouse1.count(item_name)>0:
        print("Location:Warehouse 1")   
     elif warehouse2.count(item_name)>0:
        print("Location:Warehouse2")
     answer=input("Do you wanna place an order? ""Yes or No :") 
     if answer == "Yes": 
        print("Amount available:",w1+w2)
        num_of_item=int(input("How many do you want?: ") )   
        if num_of_item<= w1+w2:
         print("your",num_of_item, item_name ,"order has been placed")      
        elif num_of_item > w1+w2:
         print("Error ,do you wanna order",w1+w2,"instead?")
         max_order=input()    
         if max_order== "yes":
            print(w1+w2, item_name,"your ordered has been placed")  
         elif answer == "No":
            print("Thank you ",user_name,"for your visit!")
         elif w1+w2==0:
            print("Not in stock") 
             
elif num == "3":
    pass
else:
    input("Operation entered is not valid\n Please enter 1 ,2 or 3 \n:")    
print("Thank you ",user_name,"for your visit!")    


# warehouse integer: The warehouse number where this item is located.
# date_of_stock date: The date and time the item was stocked.
print(x)