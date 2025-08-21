def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    if num2 == 0:
        return "❌ Division by zero not allowed"
    return num1 / num2


while True:
    print("\n===== Calculator Menu =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("===========================\n")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("✅ Exiting program... Goodbye!")
        break

    # Agar choice valid hai toh numbers lo
    if choice in ['1','2','3','4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        match choice:
            case '1':
                print("Result:", add(num1,num2))
            case '2':
                print("Result:", sub(num1,num2))
            case '3':
                print("Result:", mul(num1,num2))
            case '4':
                print("Result:", div(num1,num2))
    else:
        print("❌ Invalid choice! Please try again.")
