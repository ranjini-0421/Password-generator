import random
import string

def get_user_input(prompt, valid_inputs=None):
    while True:
        user_input = input(prompt).strip()
        if valid_inputs and user_input not in valid_inputs:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_inputs)}")
        elif not user_input:
            print("Input cannot be empty.")
        else:
            return user_input

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            return length
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def include_characters(prompt):
    return get_user_input(prompt, ["y", "n"]) == "y"

def generate_password(length, include_letters, include_numbers, include_symbols):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    length = get_password_length()
    include_letters = include_characters("Include letters? (y/n): ")
    include_numbers = include_characters("Include numbers? (y/n): ")
    include_symbols = include_characters("Include symbols? (y/n): ")
    
    try:
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        print(f"\nGenerated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
