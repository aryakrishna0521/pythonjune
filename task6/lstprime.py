numbers=[10,11,12,13,14,20,21]

for i in range(0,len(numbers)):
    for j in range(2,numbers[i]):
        if numbers[i]%j==0:
            break
        print(numbers[i])
        break
