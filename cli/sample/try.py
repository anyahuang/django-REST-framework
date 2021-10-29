from data import stock
from collections import Counter
# wh1_item =[]
# for wh_item in stock:
#   if wh_item["warehouse"]==1:
#     wh1_item.append(wh_item)
# print(wh1_item)


# for x in stock:
#   if x["state"] == "High quality":
#     if x["category"] == "Tablet":
#       if x["warehouse"] == 1:
#         print(x)
        
for x in stock:
  if x["state"] == "High quality" and x["category"] == "Tablet" and x["warehouse"] == 1 :
        print(x)
        
  elif  x["state"] == "High quality" and x["category"] == "Tablet" and x["warehouse"] == 2:
     print(x)     
     
     
                
                
       
       