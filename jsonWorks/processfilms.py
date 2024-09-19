from json import load
f=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\jsonWorks\\films.json","r")
films=load(f)
print(films)
for f in films:
    print(f.get("title"))