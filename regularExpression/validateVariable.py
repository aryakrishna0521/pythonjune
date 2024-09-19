#first letter alpha
#followed by any alpha or numerics

from re import fullmatch
variable_name=input("enter var name: ")

pattern="[a-z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,variable_name)

print("invalid" if matcher==None else "valid")

