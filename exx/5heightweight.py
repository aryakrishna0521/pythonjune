height_in_cm=int(input("height="))
weight_in_kg=int(input("weight="))
height_in_meter=height_in_cm/100
bmi=(weight_in_kg)/(height_in_meter**2)
print(bmi)
if bmi<19:
    print("under weight")
elif bmi>=19 and bmi<25:
    print("normal weight")
elif bmi>=25 and bmi<30:
    print("over weight")
else:
    print("obesity")  

    
