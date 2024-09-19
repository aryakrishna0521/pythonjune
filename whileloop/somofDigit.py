#read a num print sum of digitsnum=int(input("enter the number"))

num=int(input("enter the number"))
total=0
while(num!=0):
    digit=num%10
    num=num//10
    total=total+digit
print(total)