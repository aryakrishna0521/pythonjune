# write a pg to convert temp_in_degreecelsius to fh

temp_in_deg=20
temp_in_fh=(temp_in_deg * (9/5)) + 32
#(35°C × 9/5) + 32
print(f"{temp_in_deg} degree={temp_in_fh}fh")
