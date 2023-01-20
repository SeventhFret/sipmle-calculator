from random import choice
import sys
# VERY SIMPLE CALCULATOR

print(' WELCOME TO CALCULATOR '.center(50, '='))
    
action = sys.argv
print(action)

if action[1] == 'add':
    print()
    print('Result: ', int(input('Enter first number: ')) + int(input('Enter second number: ')))
elif action[1] == 'multiply':
    print()
    print('Result: ', int(input('Enter first number: ')) * int(input('Enter second number: ')))
elif action[1] == 'divide':
    print()
    print('Result: ', int(input('Enter first number: ')) / int(input('Enter second number: ')))
elif action[1] == 'subtract':
    print()
    print('Result: ', int(input('Enter first number: ')) - int(input('Enter second number: ')))
elif action[1] == 'joke':
    jokes = ['How many programmers does it take to change a light bulb?\nNone – It’s a hardware problem', 'A programmer walks to the butcher shop and buys a kilo of meat.\nAn hour later he comes back upset that the butcher shortchanged him by 24 grams.', 'There are three kinds of lies: Lies, damned lies, and benchmarks.', 'Debugging: Removing the needles from the haystack.']
    print(choice(jokes))


print('Got you. Bye!')