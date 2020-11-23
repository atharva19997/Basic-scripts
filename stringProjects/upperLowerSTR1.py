print('How are you?(enter GReAt or grEAT or any case)')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

# >>> spam = 'Hello, world!'
# >>> spam.islower()
# False
# >>> spam.isupper()
# False
# >>> 'HELLO'.isupper()
# True
# >>> 'abc12345'.islower()
# True
# >>> '12345'.islower()
# False
# >>> '12345'.isupper()
# False
# >>> 'Hello'.upper().lower().upper()
# 'HELLO'
# >>> 'HELLO'.lower()
# 'hello'
# >>> 'HELLO'.lower().islower()
# True
