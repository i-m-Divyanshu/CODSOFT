
def perform_addition(x, y):
    return x + y

def perform_subtraction(x, y):
    return x - y

def perform_multiplication(x, y):
    return x * y

def perform_division(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def execute_calculator():
    print("Welcome to the Arithmetic Calculator!")
    
    try:
        number_one = float(input("Enter the first number: "))
        number_two = float(input("Enter the second number: "))
    except ValueError:
        print("Oops! Please make sure you enter valid numbers.")
        return
    
    print("\nChoose one of the following operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation_choice = input("Enter the operation number (1/2/3/4): ")

    if operation_choice == '1':
        result = perform_addition(number_one, number_two)
        print(f"The sum of {number_one} and {number_two} is {result}")
    elif operation_choice == '2':
        result = perform_subtraction(number_one, number_two)
        print(f"The difference between {number_one} and {number_two} is {result}")
    elif operation_choice == '3':
        result = perform_multiplication(number_one, number_two)
        print(f"The product of {number_one} and {number_two} is {result}")
    elif operation_choice == '4':
        result = perform_division(number_one, number_two)
        print(f"The quotient of {number_one} divided by {number_two} is {result}")
    else:
        print("Invalid choice! Please select a valid operation.")

execute_calculator()
