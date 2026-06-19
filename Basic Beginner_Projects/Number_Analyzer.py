s = []

while True:
    a = int(input("Enter number: "))

    if a == 0:
        break
    else:
        s.append(a)

if len(s) > 0:
    print("Sum =", sum(s))
    print("Average =", sum(s) / len(s))
    print("Largest Number =", max(s))
else:
    print("No numbers were entered.")