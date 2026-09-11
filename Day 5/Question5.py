from copy import deepcopy
AUDIT_TRANSACTION_COUNT = 0

def create_bank_account(owner_name, initial_balance: float) -> dict:
    balance = initial_balance
    history = ["Account created with 1000.0"]

    def deposit(amount):
        nonlocal balance
        nonlocal history
        balance += amount
        history.append(f"deposit {amount}")
        global AUDIT_TRANSACTION_COUNT 
        AUDIT_TRANSACTION_COUNT += 1

    def withdraw(amount):
        nonlocal balance
        nonlocal history
        if(balance >= amount):
            balance -= amount
            history.append(f"withdraw {amount}")
            global AUDIT_TRANSACTION_COUNT
            AUDIT_TRANSACTION_COUNT += 1
        else:
            print("ValueError: Insufficient balance")

    def get_statement():
        return owner_name, balance, deepcopy(history)

    return dict(deposit = deposit, withdraw = withdraw, statement = get_statement)
 
def main():
    # Initial State
    print(AUDIT_TRANSACTION_COUNT) # Output: 0

    # Create account
    acc = create_bank_account("Arham", 1000.0)
    acc["withdraw"](2000.0)
    # Deposit
    acc["deposit"](200.0)

    # Withdraw
    acc["withdraw"](150.0)

    # Get statement
    owner, bal, txn_history = acc["statement"]()
    print(owner)       # Output: Arham
    print(bal)         # Output: 1050.0
    print(txn_history) # Output: ['Account created with 1000.0', 'deposit 200.0', 'withdraw 150.0']

    # Verify global log count
    print(AUDIT_TRANSACTION_COUNT) # Output: 2

if(__name__ == "__main__"):
    main()