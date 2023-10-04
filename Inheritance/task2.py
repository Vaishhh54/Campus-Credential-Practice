class BankAccount:
    def __init__(self):
       self.name = ""
       self.account_number = 0.0
       self.account_type = ""
       self.balance_amount = 0.0
    def addData(self):
        self.name = input("Enter Account Holder Name: ")
        self.account_number = int(input("Enter Account Number: "))
        self.account_type =input("Enter Account Type: ")
        self.balance_amount = int(input("Enter balance: "))
    def deposit(self):
        print("Bank Balance is: ",self.balance_amount)
        self.amount = int(input("Enter amount for deposit: "))
        self.balance_amount = self.balance_amount + self.amount
        print("Amount Deposited")
        print("Current balance is: ",self.balance_amount)

    def withdraw(self):
        print("Bank Balance is: ",self.balance_amount)
        self.amount = int(input("Enter amount for Withdrawn: "))
        self.balance_amount = self.balance_amount - self.amount
        print("Amount Withdrawn")
        print("Current balance is: ",self.balance_amount)
    def display(self):
        print("Account Holder Name is: ",self.name)
        print("Account Number is: ",self.account_number)
        print("Account type is: ",self.account_type)
        print("Account Balance is: ",self.balance_amount)

class SavingAccount(BankAccount):
    def withdraw(self):
        print("Bank balance is: ",self.balance_amount)
        if(self.balance_amount > 100):
            super().withdraw()
        else:
            print("Please enter sufficient amount")

s = SavingAccount()
while True:
    print("1.Enter Details")
    print("2.deposit Money")
    print("3. Withdraw Money")
    print("4.Display Information")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        s.addData()
    elif ch == 2:
        s.deposit()
    elif ch ==3:
        s.withdraw()
    elif ch == 4:
            s.display()
    else:
        print("enter valid choice")
        break
