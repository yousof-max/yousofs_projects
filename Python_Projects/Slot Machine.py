import random

def spin_row():
    symbols = ["😁", "💕", "😎", "🤑", "🤩"]
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("****************************")
    print(" ".join(row))
    print("****************************")
def get_payout(row, amount):
    multiplier = 0
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "🤑":
                multiplier = 100
            case "😎":
                multiplier = 20
            case "😁":
                multiplier = 10
            case "🤩":
                multiplier = 5
            case "💕":
                multiplier = 2
    return multiplier * amount

def main():
    balance = 100
    print("****************************")
    print("Slot Machine")
    print("Symbols: 🤑😎😁🤩💕")
    print("****************************")
    while balance > 0:
        print(f"Current Balance {balance}")
        amount = input("Enter amount to bet: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > balance:
                print("insufficient funds")
            elif amount <= 0:
                print("must be greater than 0")
            else:
                balance -= amount
                row = spin_row()
                print_row(row)
                if get_payout(row, amount) > 1:
                    payout = get_payout(row, amount)
                    balance += payout
                    print(f"YOU WON {payout}")
                else:
                    print("you lost")
        else:
            print("INVALID AMOUNT")
if __name__ == "__main__":
    main()