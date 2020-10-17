import sys
while True:
    print('Type bye to exit.')
    response = input()
    if response == 'bye':
        sys.exit()
    print('You typed ' + response + '.')
