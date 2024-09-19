number=[2,4,5,7,8,9]
# number.sort()
# print(number[-2])
largest=number[0]
second_largest=number[0]
for i in number:
    if i>largest and i>second_largest:

        second_largest=largest
        largest=i  
    elif i>second_largest and i<largest:

        second_largest=i   
          
print(second_largest)