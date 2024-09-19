
employee={"name":"arya","dept":"r&d","salary":50000,"combo_offer":1000,"extra_working_days":3}

#print all key and value
for k,v in employee.items():
    print(k,v)

#chck extra_working_days present
if "extra_working_days" in employee:
    print("present")
else:
    print("not present")
    

#net pay
if "extra_working_days" in employee:
    net_pay=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_working_days")
    print(net_pay)
else:
    net_pay=employee.get("salary")
    print(net_pay)



#fetchiing value from dictionary using key dict.get(key)
# adding new pair dict[key]=value    