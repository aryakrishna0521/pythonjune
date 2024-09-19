f=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\fileworks.py\\news.txt","r")
word_list=[w for line in f for w in line.rstrip("\n").split(" ")if w!='']

# for line in f:
#     word=line.rstrip("\n").split(" ")

#     for w in word:
#         word_list.append(w)


wc={w:word_list.count(w)for w in word_list}
# print(wc)


def get_value(key):
    return wc.get(key)
srt=sorted(wc,key=get_value,reverse=True)
print(srt)
