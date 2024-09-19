#function
#def function_name(parm1,parm2,,,,,parmn):
     #function definition
     #return value

def is_leap_year(year):
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        return True
    else:
        return False
print(is_leap_year(2024))        

       