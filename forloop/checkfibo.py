#read a number print number is fibonacci or not
number=int(input("enter number"))
previous=0
current=1 
is_fibo=False


next=current+previous
while (next<=14):
    next=current+previous
    previous=current
    current=next
    if next==number:
        is_fibo=True
        break
      
print(is_fibo)