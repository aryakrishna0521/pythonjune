text="ABBBCCBBBB"
word_count={}
for ch in text:
    if ch in word_count:         #A B C 
        print(ch,"first recursive char")   #C=C
        break
    else:
         word_count[ch]=1   #set c=key and value=1  A=1 B=1    C FOR CHAR