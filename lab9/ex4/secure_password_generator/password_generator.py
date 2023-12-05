import random
import string


def generate_password(length=12, include_special_chars=True, include_numbers=True, include_uppercase=True):
    characters = string.ascii_lowercase

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password