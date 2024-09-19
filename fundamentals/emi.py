# write a pg to calculate monthly emi
# loan amount
# tenure
# interest  rate

#p*r*(1+r)**n/(1+r)**n-1
loan_amount=100000
tenure=10
interest_rate=12

#convert yearly interest rate into monthly interest rate

r=interest_rate/(12*100)             #r=monthly interest rate
print(r)
n=tenure*12
#emi=p*r*(1+r)**n/(1+r)**n-1
one_plus_r=(1+r)**n                       #n= number of month


emi=(loan_amount*r*one_plus_r)/(one_plus_r-1)
#total 

total_payable_amount=emi*n
print(f"monthly emi={emi}")
print(f"total_payable_amount={total_payable_amount}")
total_interest_payable=total_payable_amount-loan_amount
print(f"total interest payable amount={total_interest_payable}")






