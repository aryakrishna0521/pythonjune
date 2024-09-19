text="RACECAR"
longest_palindrome=""
for i in range(0,len(text)):
    right=i
    left=i
    while (left>=0 and right<len(text)and text[right]==text[left]):
        current_palindrome=text[left:right+1]              #slice from left text to right text
        if len(current_palindrome)> len(longest_palindrome):
            longest_palindrome=current_palindrome
        left=left-1
        right=right+1
print(longest_palindrome)            
