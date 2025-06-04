import math
import os

# Operation functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(x)

# Optional: Clear the screen each time
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Store history
history = []

# Main loop
while True:
    clear_screen()
    print("=== Python Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. View History")
    print("8. Quit")

    choice = input("\nEnter your choice (1 to 8): ")

    if choice == '8':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print(" Invalid input. Press Enter to continue...")
            input()
            continue

        if choice == '1':
            result = add(num1, num2)
            operation = f"{num1} + {num2} = {result}"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = f"{num1} - {num2} = {result}"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = f"{num1} * {num2} = {result}"
        elif choice == '4':
            result = divide(num1, num2)
            operation = f"{num1} / {num2} = {result}"
        elif choice == '5':
            result = power(num1, num2)
            operation = f"{num1} ^ {num2} = {result}"

        print(" Result:", result)
        history.append(operation)

    elif choice == '6':
        try:
            num = float(input("Enter number: "))
        except ValueError:
            print(" Invalid input. Press Enter to continue...")
            input()
            continue

        result = square_root(num)
        operation = f"√{num} = {result}"
        print(" Result:", result)
        history.append(operation)

    elif choice == '7':
        print("\n Operation History:")
        if not history:
            print("No operations yet.")
        else:
            for entry in history:
                print(entry)

    else:
        print(" Invalid choice. Please choose a valid option.")

    if choice != '8':
        input("\nPress Enter to continue...")