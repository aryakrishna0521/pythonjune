
from re import fullmatch
month=input("enter month ")

pattern="(0?[1-9]|1[0-2])"
matcher=fullmatch(pattern,month)
print("invalid" if matcher==None else "valid")

