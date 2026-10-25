
#Convert km to miles and miles to km
#km → miles: miles = km × 0.621371
#miles → km: km = miles ÷ 0.621371
#kg → lb: lb = kg × 2.20462
#lb → kg: kg = lb ÷ 2.20462


while True:
    print('''
    1. km -> miles
    2. miles -> km
    3. lb -> kg
    4. kg -> lb''')
    choice = input('Choose an option: ')

    if choice == '1': 
        try:
                
            km = float(input('Enter km: '))
            miles = km * 0.621371
            print(f'{km} km is {miles:.1f} miles')
        except ValueError:
            print('Please enter a number')
            continue

    elif choice == '2':
        try:

            miles = float(input('Enter miles: '))
            km = miles / 0.621371
            print(f'{miles} miles is {km:.1f} km')
        except ValueError:
            print('Please enter a number')
            continue
    elif choice == '3':
        try:
            lb = float(input('Enter lb: '))
            kg = lb / 2.20462
            print(f'{lb} lb is {kg:.1f} kg')
        except ValueError:
            print('Please enter a number')
            continue
    elif choice == '4':
        try:
            kg = float(input('Enter kg: '))
            lb = kg * 2.20462
            print(f'{kg} kg is {lb:.1f} lb') 
        except ValueError:
            print('Please enter a number')
            continue   
    else:
        print('Input must be 1 to 4')

    while True:
        again = input('Want to do another conversion? y/n: ').lower()
        if again == 'y':
            break
        elif again == 'n':
            exit()
        else:
            print('Please enter y/n')
            






    
