def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Prevent division by zero
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def show_menu():
    print("\nSimple Calculator")
    print("-----------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")

def main():
    history = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
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

            print("Result:", result)
            history.append(operation)

        elif choice == '5':
            print("\n--- Calculation History ---")
            if history:
                for i, record in enumerate(history, 1):
                    print(f"{i}. {record}")
            else:
                print("No history yet.")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose from 1 to 6.")

if __name__ == "__main__":
    main()