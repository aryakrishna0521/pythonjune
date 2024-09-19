# 121 rev=121  so palindrome
num=(int(input("enter the number")))
result=0
org=num
while (num!=0):
    digit=num %10
    result=result*10+digit
    num=num//10
print(f"palindrome"if result==org else "non palindrome")       
