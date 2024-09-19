#try         error possibility code
#exception   error handling code
#finally     clean up process


num1=int(input("enter number1 "))
num2=int(input("enter number2 "))

try:
    result=num1/num2
    print("division result",result)
except:
    print("error occured")

print("database commit")
print("file operation")