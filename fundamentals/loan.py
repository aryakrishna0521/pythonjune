#write a pg to calculate monthly  emi

#loan amount
#tenure
#interest rate
loan_amount=100000
tenure=10   #(in yr)
interest_rate=12

#p*r*(1+r)**n/(1+r)**n-1     
# #p=loan amount
#r=monthly interest rate
#n= number of months

#interest rate to monthly interest rate

r=interest_rate/(12*100)
print(r)
n=tenure*12

one_plus_r=(1+r)**n
emi=(loan_amount*r*one_plus_r)/(one_plus_r-1)
print(f"monthly emi={emi}")

total_payable_amount=emi*n
print(f"total payable amount={total_payable_amount}")
total_interest_payable=total_payable_amount-loan_amount
print(f"total interest payable={total_interest_payable}")