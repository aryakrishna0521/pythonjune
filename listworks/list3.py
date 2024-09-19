#print a list of expenses

#print expenses>15000

#find total expenses



expenses=[10000,30000,40000,70000,12333,32000]
# expenses_count=(len(expenses))
# for i in range(0,expenses_count):
#      #print(expenses[i])
#     if expenses[i]>15000:
#         print(expenses[i])


#total expenses


total=0
for i in range(0,len(expenses)):
    total=total+expenses[i]
print(total)    

#avg

avg_expense=total/len(expenses)
print(avg_expense)


