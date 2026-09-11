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

    return dict(deposit = ) 
def main():
    ...
if(__name__ == "__main__"):
    main()