from calculator import add, subtract, multiply, divide

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "5":
        break

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice")
        continue

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        else:  # choice == "4"
            result = divide(a, b)

        print(result)
    except ValueError:
        print("Invalid number")
    except ZeroDivisionError:
        print("Cannot divide by zero")