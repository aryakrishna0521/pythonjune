
#armstrong num
#12==1^2+2^2==5 not an amstrong

num=(int(input("enter the number")))
org=num
total=0
digit_count=len(str(num))
while(num!=0):
    digit=num%10
    exponent=digit**digit_count
    total=total+exponent
    num=num//10
print(total)  

print(f" armstrong number" if org==total else " not armstrong")  




