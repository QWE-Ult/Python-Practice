Balance = 1000000

while True:
    print("### ATM Menu ###\n")
    print("\t1. Check Balance")
    print("\t2. Deposit Money")
    print("\t3. Withdraw Money")
    print("\t4. Exit")

    a = int(input("\nChoose From Above : "))

    if a == 1:
        print(f"Your Balance is : {Balance}")

    elif a == 2:
        i = int(input("Enter Amount : "))
        Balance = Balance + i
        print(f"You Deposited : {i} and Your Current Balance is {Balance}")

    elif a == 3:
        i = int(input("Enter Amount : "))

        if i <= Balance:
            Balance = Balance - i
            print(f"You withdrew : {i} and Your Current Balance is {Balance}")
        else:
            print("Insufficient Balance")

    elif a == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Insert a Valid Number")
        
        
