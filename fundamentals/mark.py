#write a pg to read stud_name and 3 marks mark1,mark2,mark3
#and print toatl mark and avg
stud_name=input("enter the student name")
mark1=(int(input("enter the mark1")))
mark2=(int(input("enter the mark2")))
mark3=(int(input("enter the mark3")))

total=(mark1)+(mark2)+(mark3)
avg_mark=total/3
print(f"student name={stud_name} total mark ={total}avg mark={avg_mark}")