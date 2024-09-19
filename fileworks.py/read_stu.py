f=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\fileworks.py\\students.txt","r")
students=[]
for stud in f:
    students.append(stud.rstrip("\n"))
print(students)    