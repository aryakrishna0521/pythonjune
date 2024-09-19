mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]
mobile_name=[mb.get("title")for mb in mobiles]
#print(mobile_name)

mobile_brand={mb.get("brand") for mb in mobiles}
#print(mobile_brand)


samsung_mobiles=[mb.get("title") for mb in mobiles if mb.get("brand")=="samsung"]
#print(samsung_mobiles)

#print mob name whose price in range 23000-40000

mob_available=[mb.get("title") for mb in mobiles if mb.get("price")in range(23000,41000)]
#print(mob_available)


#collections,kangarooo,bracket,

# max_price=0
# for mb in mobiles:
#      if mb.get("price")>max_price:
#         max_price=mb.get("price")
# costly_mobile=[mb.get("title") for mb in mobiles if mb.get("price")==max_price]
# print(costly_mobile)

def getprice(mob):
    return mob.get("price")
costly_mobile=max(mobiles,key=getprice)  
# print(costly_mobile)  

cheapest_mob=min(mobiles,key=getprice)
# print(cheapest_mob)

sorted_mobile=sorted(mobiles,key=getprice,reverse=True)
# print(sorted_mobile)


total_cost=sum([ mob.get("price") for mob in mobiles])
print(total_cost)