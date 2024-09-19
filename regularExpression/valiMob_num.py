#validate mob num with country code mandatory

from re import fullmatch
mob_num=input("enter num")
pattern="(91)[0-9]*"
matcher=fullmatch(pattern,mob_num)
print("invalid" if matcher==None else "valid")