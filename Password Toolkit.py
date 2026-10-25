import secrets
import string


def generate_password(length, use_numbers, use_symbols):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''
    for _ in range(length):
        password += secrets.choice(characters)
    return password


def check_strength(password):
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0 
    if has_digit:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_symbol:
        score += 1
    if len(password) >= 12:
        score += 1

    if score == 5:
        return 'Strong'
    elif score >= 3:
        return 'Medium'
    else:
        return 'Weak'


        
