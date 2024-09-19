#read three numbers num1 num2 num3
#print second largest
num1=(int(input("enter the first number")))            #num=1  num2=2 num3=3
num2=(int(input("enter the second number")))
num3=(int(input("enter the third number")))
if num1>num2>num3 or num3>num2>num1:            #3>2>1  or  1>2>3
    print(f"num2 {num2}is the second largest")    #2


elif num1>num3>num2 or num2>num3>num1:          #1>3>2   or   2>3>1
    print(f"num3 {num3}is the second largest")    #3


elif num3>num1>num2 or num2>num1>num3:          #3>1>2    or 2>1>3
    print(f"num1 {num1}is the second largest")    #1



# 1 4 2
# num1<num3<num2   1<2<4     2