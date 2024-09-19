words=["hello","hi","hello","hi","hi","hai"]

#print word count

# word_set=set(words)
# print(word_set)
# for w in word_set:
#     print(w,words.count(w))


word_count={}
for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)