users = {
    1: {"username": "user1", "password": "pass1", "name": "John Doe", "balance": 1000},
    2: {"username": "user2", "password": "pass2", "name": "Jane Doe", "balance": 1500},
    # other users...
}

def login():
    attempt_count = 0
    while attempt_count < 3:
        username = input("Username: ")
        user = next((u for u in users.values() if u["username"] == username), None)
        if user:
            for _ in range(3):
                password = input("Password: ")
                if password == user["password"]:
                    return user
                print("Wrong password.")
            print("You're an impostor!")
            break
        else:
            print("No such username on the list.")
        attempt_count += 1

def account_actions(user):
    while True:
        action = input("Options: 1. View balance, 2. Log out: ")
        if action == '1':
            print(f"Balance: {user['balance']} USD")
            withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
            if withdrawal_amount <= user["balance"]:
                user["balance"] -= withdrawal_amount
                print(f"Happy spending! New balance: {user['balance']} USD")
            else:
                print("Insufficient funds.")
        elif action == '2':
            break
        else:
            print("Invalid option.")

def bank_system():
    while True:
        user = login()
        if user:
            account_actions(user)

# Start the bank system
bank_system()