#print two numbers from user num1 num2
#read the largest
#if both are equal print both are equal
num1=(int(input("enter the first number")))
num2=(int(input("enter the second number")))
if num1>num2:
    print(f"{num1}is the largest number")
elif num2>num1:
    print(f"{num2} is the largest")    
else:
    print("both are equal")   