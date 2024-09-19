arr=[6,7,3,4,8,9,10]

#   [7,8,2,3,9,10,11]

mapped_list=[num+1 if num >5 else num-1 for num in arr]
print(mapped_list)



#w/o comprehension
# mapped_list=[]
# for num in arr:
#     if num>5:
#         mapped_list.append(num+1)
#     else:
#         mapped_list.append(num-1) 
# print(mapped_list)           