#kerala vehicle  num validation
#start with KL
#two digits
#alphabets (one or two)
#digits 4

from re import fullmatch

vehicle_num=input("enter the num ")

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}()-?[0-9]{4}"


matcher=fullmatch(pattern,vehicle_num)

print("invalid" if matcher==None else "valid")

