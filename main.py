# VERY SIMPLE CALCULATOR

print(' WELCOME TO CALCULATOR '.center(50, '='))

first_choise = 'yes'

while first_choise == 'yes':
    
    action = int(input('What would you like to do?\n\n•[1] Add\n•[2] Multiply\n•[3] Divide\n•[4] Subtract\n•[5] Random joke\n\n'))

    if action == 1:
        print()
        print('Result: ', int(input('Enter first number: ')) + int(input('Enter second number: ')))
    elif action == 2:
        print()
        print('Result: ', int(input('Enter first number: ')) * int(input('Enter second number: ')))
    elif action == 3:
        print()
        print('Result: ', int(input('Enter first number: ')) / int(input('Enter second number: ')))
    elif action == 4:
        print()
        print('Result: ', int(input('Enter first number: ')) - int(input('Enter second number: ')))
    elif action == 5:
        pass

    print()
    first_choise = input('Would you like to use calculator further? y/n ')
    print()

print('Got you. Bye!')