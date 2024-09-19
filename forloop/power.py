num=(int(input("enter the number")))
total=0
pattern=0
for i in range(1,num+1):
    pattern=pattern*10+num
    total=total+pattern
print(total)    
