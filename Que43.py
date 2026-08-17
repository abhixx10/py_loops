while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Exit")
    choice = int(input("Choose: "))
    if choice == 4:
        break
    a = int(input("Enter first: "))
    b = int(input("Enter second: "))
    if choice == 1:
        print("Result:", a+b)
    elif choice == 2:
        print("Result:", a-b)
    elif choice == 3:
        print("Result:", a*b)
    else:
        print("Invalid choice")