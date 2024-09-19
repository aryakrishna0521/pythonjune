text="pneumonoultramicroscopicsilicovolcanoconiosis"
vowel="aeiou"
text=text.casefold()
v_count=0
c_count=0



for ch in text:
    if vowel.count(ch)!=0:
        v_count+=1  
    else:
        c_count+=1
print(v_count)  
print(c_count)  

