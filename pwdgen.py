import random
import string

def generate_password(length=12):
    """Generate a random password with a given length."""
    # Define possible characters
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the remaining length with random characters from all categories
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to make the password unpredictable
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Example usage
password = generate_password(16)  # Generate a 16-character password
print(f"Generated Password: {password}")
