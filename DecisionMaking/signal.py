#write a pg to p

signal=(input("enter the signal"))
if signal=="red":
    print(f"stop")
elif signal=="green":
    print(f"go")
elif signal=="orange":
    print(f"wait")     
else:
    print(f"default stmt")   