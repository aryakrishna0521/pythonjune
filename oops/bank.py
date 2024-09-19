class bank:
    acno:int
    bank_name:str
    bank_bal:int
    ac_type:str

    def create_account(self,acno,ac_type):
        self.bank_name="CANARA"
        self.__bank_bal=2000
        self.acno=acno
        self.ac_type=ac_type

    def deposit(self,amount):
        self.__bank_bal+=amount
        print(f"your{self.bank_name} acc with {self.acno} has been credited with rs{amount}")

    def withdraw(self,amount):
        if amount>self.__bank_bal:
            print(f"transaction failed insufficient balance")
        else:
            self.__bank_bal-=amount
            print(f"your{self.bank_name} acc with accno {self.acno} is debited with rs{amount} available balance is{self.__bank_bal}")

user_account=bank()

user_account.create_account(101,"savings")
user_account.deposit(2000) 
user_account.withdraw(1000)








    
























