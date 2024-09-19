
# from re import finditer
# text="ababbaab"
# #count ab,position
# matcher=finditer("ab",text)                   #FINDITER== RETURNS GROUP OF OBJECT
# count=0
# for m in matcher:
#     print(m.start(),"===",m.group())
#     count+=1
# print(count)    


from re import finditer
text="pythonjangopythonjangopython"
count=0
match=finditer("python",text)
for p in match:
    count+=1
    print(p.start(),"==",p.group())
print(count)    


