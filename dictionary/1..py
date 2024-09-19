#craete a dictionary mobile with keys name,brand,price,is_available

mobile={"name":"s23","brand":"samsung","price":150000,"is_available":True}


#print name

# print(mobile["name"])   #it shows with an error msh
# print(mobile.get("name")) #if there is an error it invalid syntax and return next .


# #print all keys
# print(mobile.keys())

# #values()
# print(mobile.values())


# #items()
# for k,v in mobile.items():
#     print(k,v)

#pop()
mobile.pop("name")  #if pop call the popped  element would return
print(mobile)   

#add offer=500

mobile["offer"]=500
print(mobile)


#selling price
# selling_price=price-offerprice
if "offer" in mobile:
    selling_price=mobile.get("price")-mobile.get("offer")
    print(selling_price)
else:
    selling_price=(mobile.get("price"))
    print(selling_price) 