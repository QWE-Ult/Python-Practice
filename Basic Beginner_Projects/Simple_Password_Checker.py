password = "python123"
attempts = 0

while True:
    entered_password = input("Enter Password: ")
    attempts += 1

    if entered_password == password:
        print("Access Granted!")
        print("Attempts used:", attempts)
        break
    else:
        print("Incorrect Password. Try Again.")