year=int(input("enter the year"))
if ( year%100==0 and year%400==0)  or (year%100!=0 and year%4==0) :      #when checkin cgentury year year%400 otherwise year%4
    print(f"{year}is leap year")
else:
    print(f"{year}is not a leap year")    
   