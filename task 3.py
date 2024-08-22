import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation):
    """Generate a random password based on user preferences."""
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected. Please enable at least one character type.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    """Get user input for password generation."""
    length = int(input("Enter the desired password length: "))
    
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_punctuation = input("Include punctuation? (y/n): ").strip().lower() == 'y'

    return length, use_uppercase, use_lowercase, use_digits, use_punctuation

def main():
    length, use_uppercase, use_lowercase, use_digits, use_punctuation = get_user_input()
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "_main_":
    main()