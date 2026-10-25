

#C → F: F = C × 9 ÷ 5 + 32
#F → C: C = (F − 32) × 5 ÷ 9


while True:
    choice = input('Press 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius: ')


    if choice =='1':
        temp = float(input('Enter the temperature: '))
        x = temp*9/5+32
        print(x)
        break
    elif choice =='2':
        temp = float(input('Enter the temperature: '))
        y = (temp - 32) * 5 / 9 
        print(y)
        break
    else:
        print("Input must be a 1 or 2")
2