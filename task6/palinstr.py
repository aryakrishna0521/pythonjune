words=["madam","aba","bcb","hello","python"]
print("the palindromes are")
for i in range(0,len(words)):
    if words[i]==words[i][::-1]:
        print(words[i])