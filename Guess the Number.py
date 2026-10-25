play_again = "yes"


import random
while play_again == "yes":
 
    # 1. generate the secret number and store it
    secret_number = random.randint(1, 100)
    
    # 2. start a loop that keeps going until they guess right
    for attempt in range(5):
        print("Attempt number:", attempt)
    # 3. ask the user to guess a number    
        guess = input("Guess a number: ")
    # 4. convert the guess to an integer    
        guess = int(guess)
    # 5. check if the guess is too high, too low, or correct
        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Correct!")
            break
    else:
        print("You ran out of attempts! The number was:", secret_number)
    play_again = input("Play again? (yes/no): ")




