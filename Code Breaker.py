import random

secret_code = str(random.randint(0,9999)).zfill(4)
tries = 0
while True:
    guess = input('Take a guess of the 4 digit code: ')
    if len(guess) != 4 or not guess.isdigit():
        print(f'"{guess}" isn\'t valid - enter exactly 4 digits')
        continue
    

    tries += 1
    if guess == secret_code:
        print(f'Code cracked! Tries: {tries}')
        break
    else:
        correct_spot = 0
        for i in range(4):
            if guess[i] == secret_code[i]:
                correct_spot += 1 
        print(f'Correct spot: {correct_spot}')
        total = 0
        for d in '0123456789':
            in_code = secret_code.count(d)
            in_guess = guess.count(d)
            total += min(in_code,in_guess)
        wrong_spot = total - correct_spot
        print(f'Wrong spot: {wrong_spot}')
        print(f'Tries so far: {tries}')
    
