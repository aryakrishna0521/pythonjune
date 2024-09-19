arr=[
    [10,12],
    [20,35],
    [31,40]
]
number=[num for lst in arr for num in lst]
print(sum( number))

evens=[num for lst in arr for num in lst if num%2==0]
print(evens)

#num_gt_15
num_gt_15=[num for lst in arr for num in lst if num>15]
print(num_gt_15)


