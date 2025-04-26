class BankingSystem:

    customers = 0

    def __init__(self, name, balance):

        self.__name = name
        self.__balance = balance
        BankingSystem.customers += 1

    def check_balance(self):
        
        print("----------------------------------")
        print(f"'{self.__name}' Your current Balance is : ${self.__balance:.2f}")
        print("----------------------------------")

    def deposit(self, amount):

        if amount <= 0 :
            print("Invalid, The deopsit should be greater than Zero")
            return
        else:
            self.__balance += amount
            print("Succesfull Transaction")
        self.check_balance()

    def withdraw(self, amount):


        if self.valid_amount(amount):

            self.__balance -= amount
            print("Seccesfull Transaction")
        self.check_balance()
    
    def valid_amount(self, amount):
        if amount > self.__balance :
            print("insufficient Credit!!")
            return False
        elif amount <= 0 :
            print("Invalid, please enter an amount greater than Zero")
            return False
        return True

    def transfer_to_another_account(self, account, amount):
        
        if self.valid_amount(amount):
            self.__balance -= amount
            account.__balance += amount
        self.check_balance()

monsour = BankingSystem("Monsour", 5000)
sara = BankingSystem("Sara", 10000)

monsour.check_balance()

monsour.deposit(-183)
monsour.deposit(1500)

monsour.withdraw(-288)
monsour.withdraw(8000)
monsour.withdraw(1200)

monsour.transfer_to_another_account(sara, 2999)
sara.check_balance()