import random
import string

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage: generate a password of default length 12
print("Generated password:", generate_password())

# Example usage: generate a password of custom length 16
print("Generated password (length 16):", generate_password(16))
