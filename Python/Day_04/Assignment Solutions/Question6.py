from copy import deepcopy
from pprint import pprint
class AccountNotFoundError(Exception):
    def __init__(self, account):
        super().__init__(f"Account {account} not found.")
        self.account = account

class InvalidTransactionError(Exception):
    def __init__(self, transaction_type):
            super().__init__(f"Invalid transaction type: {transaction_type}.")
            self.transaction_type = transaction_type

class OverdraftError(Exception):
    def __init__(self, account, balance, amount):
        super().__init__(f"Insufficient funds. Account {account} has balance {balance}, requested {amount}.")
        self.account = account
        self.balance = balance
        self.amount = amount

def process_transaction_batch(accounts, batch_list, log_path):
    accounts_copy = deepcopy(accounts)
    try:
        for transaction in batch_list:
            account_ID = transaction["acc"]
            transaction_type = transaction["type"]
            transaction_amount = transaction["amt"]

            if(account_ID not in accounts_copy):
                raise AccountNotFoundError(account_ID) 
            account = transaction["acc"]

            if(transaction_type not in ("deposit", "withdraw")):
                raise InvalidTransactionError(transaction_type)

            if transaction_amount <= 0:
                raise InvalidTransactionError(
                    f"Transaction amount must be positive: {transaction_amount}"
                )

            if(transaction["type"] == "withdraw"):
                balance = accounts_copy[account]
                if(transaction_amount > balance):
                    raise OverdraftError(account_ID, balance, transaction_amount)
                accounts_copy[account] -= transaction_amount
            else:
                accounts_copy[account] += transaction_amount 

        print("All the transactions are successfully executed")    
        accounts.clear()
        accounts.update(accounts_copy)
    
    except AccountNotFoundError as e:
        print(f"Error: {e}")
        return
    except OverdraftError as e:
        print(f"Error: {e}")
        return
    except InvalidTransactionError as e:
        print(f"Error: {e}")
        return 

               
def main():
    accounts = {"ACC01": 500.0, "ACC02": 200.0}
    batch_list = [
        {"acc": "ACC01", "type": "deposit", "amt": 600.0},
        {"acc": "ACC02", "type": "withdraw", "amt": -500.0}
    ]
    log_path = input("Enter log path: ")
    process_transaction_batch(accounts, batch_list, log_path)
    pprint(accounts)
main()