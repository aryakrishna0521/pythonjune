#read three numbers from user num1 num2 num3
#print numbers in sorted order
num1=(int(input("enter the first number")))
num2=(int(input("enter the second number")))
num3=(int(input("enter the third number")))
if num1<num2<num3:
    print(num1,num2,num3)
elif num2<num1<num3:
    print(num2,num1,num3)  
elif num3<num2<num1:
    print(num3,num2,num1)   
elif num2<num3<num1:
    print(num2,num3,num1) 
elif num3<num1<num2:
    print(num3,num1,num2)  
elif num1<num3<num2:
    print(num1,num3,num2)            
# print(sorted([a,b,c]))    logic2