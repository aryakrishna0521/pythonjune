
number=[3,5,9,8,4,2,1,0]
# number.sort()
# print(number[1])       #using method


smallest_num=number[0]
second_smallest=number[1]

for i in number:
    if i<second_smallest and i<smallest_num:
        second_smallest=smallest_num
        smallest_num=i
    elif i<second_smallest and i>smallest_num:
        second_smallest=i
print(second_smallest)        



