import random
import string

def generate_password(length):
    # Define characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choice()
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get user input for the desired password length
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive integer.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Generate and display the password
password = generate_password(length)
print("Generated Password:", password)
