arr=[10,11,12,13,14,15,16,17]
  #   0  1  2  3  4  5  6  7

#odd_pos=[11,13,15,17]
# reverse=[17,15,13,11]
# o/p=[10,17,12,15,14,13,16,11]

left=1
length=len(arr)
if length%2!=0:
    right=length
else:
    right=length-1

while(left<right):
    (arr[left],arr[right])=(arr[right],arr[left])
    left=left+2
    right=right-2
print(arr)    






