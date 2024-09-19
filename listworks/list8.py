# unique 

num=[1,2,5,3,4,6,5,6,7,7,8,2,9]
unique_list=[]
for i in num:
    if num.count(i)==1:
        unique_list.append(i)
print(unique_list)


