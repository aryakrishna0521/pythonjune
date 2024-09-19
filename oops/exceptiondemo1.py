num1=int(input("enter num1"))
num2=(input("enter num2"))

try:
    result=num1+num2
    print(result)

except Exception as e:
    # print(e)
    result=int(num1)+int(num2)
    print(result)


finally:
    print("db commit")