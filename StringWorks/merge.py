word1="PQRST"
word2="ABC"
merged_string=""

smallest_word=word1 if len(word1)<len(word2) else word2

for i in range(0,len(smallest_word)):

    merged_string=merged_string+word1[i]+word2[i]

if len(word1)>len(word2) :
    balance=word1[len(smallest_word):]
else:
    balance=word2[len(smallest_word):]

merged_string=merged_string+balance
print(merged_string)

       

    
