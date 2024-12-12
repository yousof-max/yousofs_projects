import time

def rounded(num):
    return round(num, 2)

def show_balance(balance):
    print(f"Your balance is ${balance}")

def deposit():
    while True:
        money_deposited = input("How much would you like to deposit: ")
        try:
            float(money_deposited)
            money_deposited = float(money_deposited)
            if round(money_deposited, 2) != money_deposited:
                print("No more than two decimal places are allowed")
            else:
                break
        except ValueError:
            print("Enter a valid numeric value")
    return money_deposited
def withdraw(balance):
    while True:
        money_withdrawn = input("How much would you like to withdraw (b to return): ")
        if money_withdrawn == "b":
            break
        else:
            try:
                float(money_withdrawn)
                money_withdrawn = float(money_withdrawn)
                if round(money_withdrawn, 2) != money_withdrawn:
                    print("No more than two decimal places are allowed")
                elif balance - money_withdrawn < 0:
                    print("You are going to go into debt if you do")
                else:
                    break
            except ValueError:
                print("Enter a valid numeric value")
    return money_withdrawn
def main():
    balance = 0
    is_running = True
    while is_running:
        print("-------Welcome this is a bank-------")
        print("****************************")
        print("""Show Balance = 1
Deposit = 2 
Withdraw = 3
Exit = 4
****************************""")
        option = input("Options (1, 2, 3, 4): " )
        if option.isdigit():
            match int(option):
                case 1:
                    show_balance(balance)
                    time.sleep(1)
                case 2:
                    amount_deposited = deposit()
                    balance += amount_deposited
                    print(f"You have deposited ${amount_deposited}")
                    time.sleep(1)
                case 3:
                    amount_withdrawn = withdraw(balance)
                    if amount_withdrawn == "b":
                        print()
                    else:
                        print(f"Your have withdrawn ${amount_withdrawn} from your {balance}")
                        balance -= amount_withdrawn
                        time.sleep(1)
                case 4:
                    is_running = False
                case _:
                    print("INVALID OPTION TRY AGAIN")
                    time.sleep(0.5)
        else:
            print("INVALID OPTION TRY AGAIN")
            time.sleep(0.5)
if __name__ == '__main__':
    main()