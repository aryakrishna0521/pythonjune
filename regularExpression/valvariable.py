#variable name

#first char must be an alpha k to m
#second letter must be number that is / by 3
#followed by any num or alpha and @

from re import fullmatch

variable_name=input("enter the variable name: ")

pattern="[k-m][369][a-zA-z0-9@]*"

matcher=fullmatch(pattern,variable_name)

print("invalid" if matcher==None else "valid")


