class BankAccount:
    def __init__(self, acct_no, starting_balance):
        self.__acct_no = 0
        self.__balance = 0.0
        self.set_account_number(acct_no)
        self.set_balance(starting_balance)
        
    def __is_valid_amount(self, amount):
        return isinstance(amount, (int, float)) and amount >= 0
 
    def set_account_number(self, new_number):
        if isinstance(new_number, int) and new_number > 0:
            self.__acct_no = new_number
        else:
            print("Invalid account number. It must be a positive whole number.")
 
    def set_balance(self, new_balance):
        if self.__is_valid_amount(new_balance):
            self.__balance = float(new_balance)
        else:
            print("Warning: the balance must not be a negative number.")
 
    @property
    def account_number(self):
        return self.__acct_no
 
    @property
    def balance(self):
        return self.__balance
 
    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:,.2f}")
 
a1 = BankAccount(12345, 1000)
 
print("Account 1")
a1.display()
 
print("\nUpdate balance to -100")
a1.set_balance(-100)
a1.display()
 
print("\nUpdate balance to 2500.5")
a1.set_balance(2500.5)
a1.display()
 
print("\nUpdate account number to 67890")
a1.set_account_number(67890)
a1.display()
