start=1
sum=0
while(start<=100):
    if start%2==0:
       sum=sum+start
    start=start+1
print(sum)            

sum=0
for i in range(2,101,2):
    sum=sum+i
print(sum)