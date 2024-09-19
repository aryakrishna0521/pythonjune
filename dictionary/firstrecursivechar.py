
text="hello hai hello hai"
#word_count
#step1:split the string
words=text.split(" ")
print(words)
word_count={}
for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)        
