from json import load
f=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\jsonWorks\\data.json","r")

products=load(f)
print(products)

for p in products:
    print(p.get("title"))