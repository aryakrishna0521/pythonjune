numbers=[10,11,12,34,43,54,19,78,42]

#print number of objects
print(len(numbers))

#even numbers


for i in range(0,len(numbers)):
    if numbers[i]%2==0:
        print(numbers[i])

#total


total=0
for i in range(0,len(numbers)):
    total=total+numbers[i]
print(total)


#odd
odd_total=0
for i in range(0,len(numbers)):
    if numbers[i] %2!=0:
        odd_total+=numbers[i]

print(odd_total)

