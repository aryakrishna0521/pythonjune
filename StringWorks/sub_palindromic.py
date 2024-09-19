# palindromic substring from given string

text="RACECAR"  
longest_palindrome=""

for i in range(0,len(text)):
    left=i
    right=i
    while (text[left]==text[right] and left>=0 and right<len(text)):
        current_palindrome=text[left:right+1]  #slice    
        print(current_palindrome)

        left=left-1
        right= right+1
