def calculate(first_number: float, second_number: float, operation: str):
    match operation:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '/':
            if second_number == 0:  # Handle division by zero
                return "Division by zero is not allowed"
            return first_number / second_number
        case '*':
            return first_number * second_number
        case '^':
            return first_number ** second_number  # ** for exponentiation
        case _:
            return "The operation is invalid"


def get_user_math():
    print("Hello, this is a basic calculator in Python to handle basic mathematical operations.\n")
    print("==============================================================================\n")

    try:
        # Converting inputs to numbers
        first_number = float(input("Please enter your first number: "))
        operation = input("Please enter your operation (+, -, *, /, ^): ")
        second_number = float(input("Please enter your last number: "))
        
        print(f"\nThank you. Here is the result of {first_number} {operation} {second_number}.\n")
        print("==============================================================================\n")
        
        result = calculate(first_number=first_number, second_number=second_number, operation=operation)
        print(f"The result of {first_number} {operation} {second_number} is {result}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")


get_user_math()
