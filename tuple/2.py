numbers=[1,2,[3,(100,200,300),4],5,6]
print(numbers)
num=numbers[2][1]
new_num=list(num)
new_num.insert(1,150)
#print(new_num)
#print(tuple(new_num))
numbers[2][1]=tuple(new_num)
#print(numbers)


list_num=numbers[2]
list_num.pop()
#print(list_num)
list_num.insert(1,4)
#print(list_num)
list_num=numbers[2]
print(numbers)
