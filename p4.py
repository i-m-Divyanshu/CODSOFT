import random
import string

def create_random_password(password_length):

    lower_case_chars = string.ascii_lowercase
    upper_case_chars = string.ascii_uppercase
    numeric_chars = string.digits
    special_chars = string.punctuation

    combined_chars = lower_case_chars + upper_case_chars + numeric_chars + special_chars


    password = ''.join(random.choice(combined_chars) for _ in range(password_length))

    return password

def generate_secure_password():
    print("Welcome to the Secure Password Generator!")

    while True:
        try:
            length = int(input("Please enter the desired password length (e.g., 12): "))
            if length < 8:
                print("For better security, it's recommended to have at least 8 characters.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    password = create_random_password(length)

    print(f"\nYour generated secure password is: {password}")

generate_secure_password()
