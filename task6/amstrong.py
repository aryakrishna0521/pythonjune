numbers=[151,153,154,370,371,3712,373,1634,1635]
print("amstrong numbers are")
for i in range(0,len(numbers)):
    total=0
    num=numbers[i]
    count=len(str(num))
    while (num!=0):
        digit=num%10
        sum=digit**count
        total=total+sum
        num=num//10
    if numbers[i]==total:
        print(numbers[i])
