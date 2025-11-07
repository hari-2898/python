class BankAccount:
    def getdata(self, name, accountnumber, account_type, balance):
        self.name = name
        self.accountnumber = accountnumber
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("Total balance =", self.balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance. Available balance =", self.balance)
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Balance after withdrawal =", self.balance)
name = input("Enter the name: ")
acc_number = int(input("Enter the account number: "))
acc_type = input("Account Type: ")
balance = int(input("Initial balance: "))
acc = BankAccount()
acc.getdata(name, acc_number, acc_type, balance)
deposit_amt = int(input("Enter amount to deposit: "))
acc.deposit(deposit_amt)
withdraw_amt = int(input("Enter amount to withdraw: "))
acc.withdraw(withdraw_amt)
