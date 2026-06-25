bal = 1000

while True:
    print("\n1 → Balance")
    print("2 → Deposit")
    print("3 → Withdraw")
    print("4 → Exit")

    a = int(input("Enter from Above: "))

    match a:
        case 1:
            print("Your Balance is:", bal)

        case 2:
            b = int(input("Enter the Amount: "))
            bal += b
            print("Deposit Successful")

        case 3:
            c = int(input("Enter Amount: "))
            if c > bal:
                print("Insufficient Balance")
            else:
                bal -= c
                print("Withdrawal Successful")

        case 4:
            print("Thank you for using the ATM")
            break

        case _:
            print("Invalid Choice")