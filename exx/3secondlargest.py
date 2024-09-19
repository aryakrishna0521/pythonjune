num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
num3=int(input("enter the number3"))
if num2>num1>num3 or num3>num1>num2:
    print(f"num1 {num1} is second lrgest")
elif num1>num2>num3 or num3>num2>num1:
    print(f"num2 {num2}is second largest")
elif num1>num3>num2 or num2>num3>num1:   
    print(f"num3 {num3}is second largest")   

    
     