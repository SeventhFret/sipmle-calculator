from random import choice

# VERY SIMPLE CALCULATOR

print(' WELCOME TO CALCULATOR '.center(50, '='))

first_choise = 'y'

while first_choise == 'y':
    
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
        jokes = ['How many programmers does it take to change a light bulb?\nNone – It’s a hardware problem', 'A programmer walks to the butcher shop and buys a kilo of meat.\nAn hour later he comes back upset that the butcher shortchanged him by 24 grams.', 'There are three kinds of lies: Lies, damned lies, and benchmarks.', 'Debugging: Removing the needles from the haystack.']
        print(choice(jokes))
    print()
    first_choise = input('Would you like to use calculator further? y/n ')
    print()

print('Got you. Bye!')