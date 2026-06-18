while True:
    print("""
    ==============================
          SIMPLE CALCULATOR
    ==============================
    
    1. Addition        (+)
    2. Subtraction     (-)
    3. Multiplication  (*)
    4. Division        (/)
    5. Floor Division  (//)
    6. Modulus         (%)
    7. Exit
    
    ==============================
    """)
    
    choice = int(input("Choose an option (1-7): "))
    
    if choice == 7:
            print("Calculator Closed.")
            break
        
    
    count = int(input("How many numbers do you want to use? "))

    result = int(input("Enter number 1: "))

    for i in range(2, count + 1):
        num = int(input(f"Enter number {i}: "))

        if choice == 1:
            result += num

        elif choice == 2:
            result -= num

        elif choice == 3:
            result *= num

        elif choice == 4:
            result /= num

        elif choice == 5:
            result //= num

        elif choice == 6:
            result %= num

        else:
            print("Invalid Choice")
            break

    else:
        print("Answer:", result)

