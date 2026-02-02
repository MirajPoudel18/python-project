# 4. Simple Banking System
# Build a banking system with functions for:

# Create account (with account number generation)
# Deposit money
# Withdraw money (with balance check)
# Check balance
# Transaction history

import datetime

# Global dictionary to store all accounts
accounts = {}

def generate_account_number():
    """Generate unique account number"""
    if not accounts:
        return "ACC001"
    else:
        last_acc = list(accounts.keys())[-1]
        number = int(last_acc[3:]) + 1
        return f"ACC{number:03d}"

def create_account(name, initial_deposit=0):
    """Create a new bank account"""
    acc_number = generate_account_number()
    
    accounts[acc_number] = {
        "name": name,
        "balance": initial_deposit,
        "transactions": []
    }
    
    # Record initial deposit if any
    if initial_deposit > 0:
        transaction = {
            "type": "Initial Deposit",
            "amount": initial_deposit,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance_after": initial_deposit
        }
        accounts[acc_number]["transactions"].append(transaction)
    
    print(f"\n✅ Account created successfully!")
    print(f"Account Number: {acc_number}")
    print(f"Account Holder: {name}")
    print(f"Initial Balance: ${initial_deposit}")
    
    return acc_number

def deposit(acc_number, amount):
    """Deposit money into account"""
    
    # Validation
    if acc_number not in accounts:
        print("❌ Account not found!")
        return False
    
    if amount <= 0:
        print("❌ Deposit amount must be positive!")
        return False
    
    # Update balance
    accounts[acc_number]["balance"] += amount
    
    # Record transaction
    transaction = {
        "type": "Deposit",
        "amount": amount,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "balance_after": accounts[acc_number]["balance"]
    }
    accounts[acc_number]["transactions"].append(transaction)
    
    print(f"\n✅ Deposit successful!")
    print(f"Amount deposited: ${amount}")
    print(f"New balance: ${accounts[acc_number]['balance']}")
    
    return True

def withdraw(acc_number, amount):
    """Withdraw money from account"""
    
    # Validation
    if acc_number not in accounts:
        print("❌ Account not found!")
        return False
    
    if amount <= 0:
        print("❌ Withdrawal amount must be positive!")
        return False
    
    if accounts[acc_number]["balance"] < amount:
        print(f"❌ Insufficient balance!")
        print(f"Current balance: ${accounts[acc_number]['balance']}")
        print(f"Attempted withdrawal: ${amount}")
        return False
    
    # Update balance
    accounts[acc_number]["balance"] -= amount
    
    # Record transaction
    transaction = {
        "type": "Withdrawal",
        "amount": amount,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "balance_after": accounts[acc_number]["balance"]
    }
    accounts[acc_number]["transactions"].append(transaction)
    
    print(f"\n✅ Withdrawal successful!")
    print(f"Amount withdrawn: ${amount}")
    print(f"New balance: ${accounts[acc_number]['balance']}")
    
    return True

def check_balance(acc_number):
    """Check account balance"""
    
    if acc_number not in accounts:
        print("❌ Account not found!")
        return None
    
    balance = accounts[acc_number]["balance"]
    name = accounts[acc_number]["name"]
    
    print(f"\n--- Account Balance ---")
    print(f"Account Number: {acc_number}")
    print(f"Account Holder: {name}")
    print(f"Current Balance: ${balance}")
    
    return balance

def transaction_history(acc_number):
    """Display transaction history"""
    
    if acc_number not in accounts:
        print("❌ Account not found!")
        return
    
    transactions = accounts[acc_number]["transactions"]
    
    if not transactions:
        print("\n📋 No transactions yet!")
        return
    
    print(f"\n--- Transaction History for {acc_number} ---")
    print(f"Account Holder: {accounts[acc_number]['name']}\n")
    
    for i, txn in enumerate(transactions, 1):
        print(f"{i}. {txn['type']}")
        print(f"   Amount: ${txn['amount']}")
        print(f"   Date: {txn['date']}")
        print(f"   Balance After: ${txn['balance_after']}")
        print("-" * 40)

def display_all_accounts():
    """Display all accounts"""
    
    if not accounts:
        print("\n📋 No accounts in the system!")
        return
    
    print("\n--- All Accounts ---")
    for acc_num, acc_data in accounts.items():
        print(f"{acc_num}: {acc_data['name']} - Balance: ${acc_data['balance']}")

# Main Menu
def main():
    while True:
        print("\n" + "="*50)
        print("       SIMPLE BANKING SYSTEM")
        print("="*50)
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Display All Accounts")
        print("7. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            name = input("Enter account holder name: ")
            initial = float(input("Enter initial deposit (0 if none): "))
            create_account(name, initial)
        
        elif choice == "2":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            deposit(acc_num, amount)
        
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            withdraw(acc_num, amount)
        
        elif choice == "4":
            acc_num = input("Enter account number: ")
            check_balance(acc_num)
        
        elif choice == "5":
            acc_num = input("Enter account number: ")
            transaction_history(acc_num)
        
        elif choice == "6":
            display_all_accounts()
        
        elif choice == "7":
            print("\n👋 Thank you for using our banking system!")
            break
        
        else:
            print("❌ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()