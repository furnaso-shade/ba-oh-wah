def balance(currentbalance):
    print(f'''
_____________________________________
your balance is {currentbalance:.2f}
--------------------------------------''')

def deposit(currentbalance):
    deposit = float(input("enter your deposit amount: "))
    currentbalance += deposit
    print(f'''
_____________________________________
you have deposited rupees {deposit:.2f} only
--------------------------------------''')
    return currentbalance

def withdraw(currentbalance):
    withdraw = float(input("enter your required money to be withdrawn: "))
    currentbalance -= withdraw
    print(f'''
_____________________________________
you have withdrawn rupees {withdraw:.2f} only
--------------------------------------''')
    return currentbalance

def main():
    currentbalance = 0.0
    while True:
        program = int(input("""____________________
WELCOME TO SBI
what brings you here today?
enter a number:
1. Check Balance
2. Deposit Paisa
3. Withdraw Paisa
4. Exit
____________________
"""))
        match program:
            case 1:
                balance(currentbalance)
            case 2:
                currentbalance = deposit(currentbalance)
            case 3:
                currentbalance = withdraw(currentbalance)
            case 4:
                break
            case _:
                print("enter a valid input")

if __name__ == '__main__':
    main()