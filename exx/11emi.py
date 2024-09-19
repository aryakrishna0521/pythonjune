#loan amnt ,
# tenure, 
# interest rate
loan_amount=(int(input("loan amount:")))
tenure=int(input("tenure:"))
interest_rate=int(input("interest rate:"))
r=interest_rate/(12*100)
print(r)
n=tenure*12
#emi=p*r*(1+r)**n/(1+r**n)-1
one_plus_r=(1+r)**n
emi=((loan_amount)*r*(one_plus_r)/(one_plus_r-1))
print(f"monthly emi is {emi}")
total_payable_amount=emi*n
print(f"total payable amount is{total_payable_amount}")
total_interest_payable=total_payable_amount-loan_amount
print(f"total interest payable is {total_interest_payable}")


