import random
import string

class PasswordGenerator:
    def __init__(self):
        pass

    def generate_password(self, length, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
        characters = ""
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if not characters:
            return "Error: Please select at least one character type (uppercase, lowercase, digits, or symbols)."

        password_chars = []
        if include_uppercase:
            password_chars.append(random.choice(string.ascii_uppercase))
        if include_lowercase:
            password_chars.append(random.choice(string.ascii_lowercase))
        if include_digits:
            password_chars.append(random.choice(string.digits))
        if include_symbols:
            password_chars.append(random.choice(string.punctuation))

        remaining_length = length - len(password_chars)
        if remaining_length < 0:
            password_chars = password_chars[:length]
            remaining_length = 0

        for _ in range(remaining_length):
            password_chars.append(random.choice(characters))

        random.shuffle(password_chars)

        return "".join(password_chars)

def main():
    generator = PasswordGenerator()

    print("--- Python Password Generator ---")

    while True:
        try:
            length = int(input("Enter desired password length in digit format: "))
            if length <= 0:
                print("Password length must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number for length.")

    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    generated_password = generator.generate_password(
        length,
        include_uppercase,
        include_lowercase,
        include_digits,
        include_symbols
    )

    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()