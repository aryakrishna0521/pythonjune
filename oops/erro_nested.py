num1=int(input("enter number1 "))
num2=int(input("enter number2 "))

try:
    result=num1/num2
    print("division result",result)
except Exception as e:
    num2=int(input(" enter number2 "))  
    result=num1/num2
    print(result)

 

    
finally:
    print("database commit")
    print("file operation")