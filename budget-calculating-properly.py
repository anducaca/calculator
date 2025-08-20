import json
import os

DATA_FILE = "budget_data.json"


def load_data():
    """Load balance and transactions from a file (if it exists)."""
    if not os.path.isfile(DATA_FILE):
        # File doesn’t exist, so start with empty/default values
        return 0.0, []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return data.get("balance", 0.0), data.get("transactions", [])


def save_data(balance, transactions):
    """Save balance and transactions to a file."""
    data = {
        "balance": balance,
        "transactions": transactions
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def main():
    # Load existing data (if any)
    balance, transactions = load_data()

    # If no balance was previously stored, ask the user to enter one
    if balance == 0.0 and not transactions:
        balance = float(input("Enter your current bank balance: "))

    while True:
        print("\n--- Budget Tracking Menu ---")
        print("1. Add a new purchase")
        print("2. View all purchases")
        print("3. Delete a purchase")
        print("4. View balance")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            description = input("Describe what you bought: ")
            date = input("And what date was this? (e.g. 2025-08-26): ")
            amount = float(input("How much did this cost? "))

            transactions.append({"description": description, "date": date, "amount": amount})
            balance -= amount
            save_data(balance, transactions)
            print("Thank you. Purchase added and saved.")

        elif choice == "2":
            if not transactions:
                print("No purchases made yet.")
            else:
                print("\n--- Transaction List ---")
                for idx, txn in enumerate(transactions, start=1):
                    print(f"{idx}. {txn['date']}  -  {txn['description']} : {txn['amount']}")

        elif choice == "3":
            if not transactions:
                print("No purchases to delete.")
            else:
                print("\n--- Delete Purchase ---")
                for idx, txn in enumerate(transactions, start=1):
                    print(f"{idx}. {txn['date']}  -  {txn['description']} : {txn['amount']}")
                index = int(input("Enter the number of the transaction to delete: "))
                
                # Adjust balance and delete the transaction
                if 1 <= index <= len(transactions):
                    removed = transactions.pop(index - 1)
                    balance += removed["amount"]
                    save_data(balance, transactions)
                    print("Purchase deleted and balance updated.")
                else:
                    print("Invalid index.")

        elif choice == "4":
            print(f"Current balance: {balance}")

        elif choice == "5":
            print("Auf Wiedersehen!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
