from json import load
f=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\jsonWorks\\products.json",encoding="UTF-8")
items=load(f)
#print(items)
# print(len(items))


items_titles=[i.get("title") for i in items]
# print(items_titles)


jewel=[c.get("title") for c in items if c.get("category")=="jewelery" ]  
# print(jewel)

product_above_hundred=[p.get("title")for p in items if p.get("price")>100]
# print(product_above_hundred)

product_range=[p.get("title")for p in items if p.get("price")>=100 and p.get("price")<=150]
# print(product_range)

#product with highest coount of reviews

def get_rating(dic):
    return dic.get("rating").get("count")
max_reviews=max(items,key=get_rating)
# print(max_reviews.get("title"),max_reviews.get("rating").get("count"))

min_reviews=min(items,key=get_rating)
print(min_reviews.get("title"),min_reviews.get("rating").get("count"))