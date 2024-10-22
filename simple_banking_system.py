# This script simulates a simple banking system with four options:
# 1. Make a deposit: Allows the user to deposit an amount, which is added to the balance.
# 2. Make a withdrawal: Allows the user to withdraw an amount, with a maximum limit of $1,500. If the withdrawal exceeds this limit, it is denied.
# 3. Obtain balance: Displays the current balance, rounded to two decimal places.
# 4. Quit: Exits the program.
# The user can repeatedly choose options until they decide to quit.

balance = 1000

print("Options\n1.Make a Deposit\n2.Make a withdrawal\n3.Obtain Balance\n4.Quit")

while True:
    choice = input("Make a selection from the options menu: ")
    if choice == "1":
        deposit = float(input("Enter amount of deposit: "))
        balance = balance + deposit
        print("Deposit Processed")
    elif choice == "2":
        while True:
            wd = float(input("Enter amount of withdrawal: "))
            if wd <= 1500:
                
                balance = balance - wd
                print("Withdrawal Processed.")
                break
            else:
                print("Denied. Maximum Withdrawal is $1,500.00")
            
    elif choice == "3":
        print("Balance: ","$" + str(round(balance, 2)))
    else:
        break
    
