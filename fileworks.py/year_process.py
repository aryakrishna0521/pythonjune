f_read=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\fileworks.py\\years.txt")
f_century=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\fileworks.py\\century.txt","w")
f_noncen=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\fileworks.py\\non_century.txt","w")
for year in f_read:
    y=(int(year.rstrip("\n")))
    if y%100==0:
        f_century.write(str(y)+"\n")
    else:
        f_noncen.write(str(y)+"\n")    
