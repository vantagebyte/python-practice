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

while True:
    print('1. Generate a password')
    print('2. Check password strength')
    print('3. Quit')
    choice = input('Choose an option: ')
    if choice == '3':
        print('Goodbye')
        break
    elif choice == '1':
        try:
            length = int(input('Password length: '))
        except ValueError:
            print('Please enter a number')
            continue
        use_numbers = input('Include numbers? (y/n)').lower() == 'y'
        use_symbols = input('Include symbols? (y/n)').lower() == 'y'
        password = generate_password(length, use_numbers, use_symbols)  
        print(password)
    elif choice == '2':
        password = input('Enter password: ')
        strength = check_strength(password)
        print(f'Strength: {strength}')

    else:
        print('Please choose 1, 2 or 3')
    
        
