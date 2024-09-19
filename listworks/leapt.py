

years=[1000,1002,2000,2004,2001,2008,2016,2028,1800]

# for i in range(0,len(years)):
#     year=years[i]
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         print(years[i])

for i in range(0,len(years)):
    year=years[i]
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(years[i])