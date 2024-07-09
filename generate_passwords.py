import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    # Define the character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation  # Includes punctuation symbols

    # Combine all character sets
    all_characters = lower_case + upper_case + digits + symbols

    # Ensure password has at least one of each type
    password = (
        random.choice(lower_case) +
        random.choice(upper_case) +
        random.choice(digits) +
        random.choice(symbols) +
        ''.join(random.choice(all_characters) for _ in range(length - 4))
    )

    # Shuffle the password characters to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    
    if num_passwords <= 0:
        print("Number of passwords should be greater than zero.")
        return
    
    print(f"Generating {num_passwords} passwords:")
    passwords = []
    
    for i in range(1, num_passwords + 1):
        while True:
            try:
                length = int(input(f"Enter the length of Password #{i}: "))
                if length < 3:
                    print("Minimum length of password should be 3. Please enter again.")
                    continue
                else:
                    passwords.append(generate_password(length))
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password #{idx}: {password}")

if __name__ == "__main__":
    main()
