import sys

class Info:
    def __init__(self, bank_name, account_holder, account_id, balance):
        self.bank_name = bank_name
        self.account_holder = account_holder
        self.account_id = account_id
        self.balance = balance
    
    def display_account_info(self):
        print(f"\n🏦 Bank: {self.bank_name}")
        print(f"👤 Account Holder: {self.account_holder}")
        print(f"🆔 Account ID: {self.account_id}")
        print(f"💰 Balance: ₹{self.balance:.2f}")

class UserAction(Info):
    def __init__(self, bank_name, account_holder, account_id, balance):
        super().__init__(bank_name, account_holder, account_id, balance)

    def debit(self):
        amount = int(input("Enter the amount to withdraw: ₹"))
        if amount <= self.balance:
            self.balance -= amount
            print(f"✅ Withdrawn ₹{amount}. Remaining Balance: ₹{self.balance:.2f}")
        else:
            print("❌ Insufficient balance.")

    def deposit(self):
        amount = int(input("Enter the amount to deposit: ₹"))
        self.balance += amount
        print(f"✅ Deposited ₹{amount}. Updated Balance: ₹{self.balance:.2f}")

class BankSystem:
    def __init__(self):
        self.customers = {}

    def add_customer(self):
        name = input("Enter account holder's name: ")
        account_id = int(input("Create a unique account ID: "))
        initial_balance = float(input("Enter initial balance: ₹"))
        if account_id in self.customers:
            print("⚠️ Account ID already exists.")
        else:
            self.customers[account_id] = UserAction("Acme Bank", name, account_id, initial_balance)
            print(f"✅ Customer '{name}' added successfully.")

    def perform_action(self):
        account_id = int(input("Enter your account ID: "))
        user = self.customers.get(account_id)
        if not user:
            print("❌ Account not found.")
            return
        
        user.display_account_info()
        while True:
            action = input("\nChoose action: deposit / debit / exit: ").lower()
            if action == 'deposit':
                user.deposit()
            elif action == 'debit':
                user.debit()
            elif action == 'exit':
                print("👋 Exiting account operations.")
                break
            else:
                print("⚠️ Invalid action.")

def main():
    bank = BankSystem()
    print("💳 Welcome to the PythonGeeks Multi-Customer Bank System!")

    while True:
        print("\n🏁 Main Menu:")
        print("1. Add New Customer")
        print("2. Access Customer Account")
        print("3. Exit")

        choice = input("Select an option (1-3): ")
        if choice == "1":
            bank.add_customer()
        elif choice == "2":
            bank.perform_action()
        elif choice == "3":
            print("🔒 Exiting program. Thank you!")
            sys.exit()
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()