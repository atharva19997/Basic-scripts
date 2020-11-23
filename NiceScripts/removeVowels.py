import pprint

text = input()
newString = ''  # for remaining string
# defining dictionary
vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# Checking for vowels in text
for char in text:
    if char == 'a':
        vowel['a'] += 1
    elif char == 'e':
        vowel['e'] += 1
    elif char == 'i':
        vowel['i'] += 1
    elif char == 'o':
        vowel['o'] += 1
    elif char == 'u':
        vowel['u'] += 1
# returning remaining text
    if char not in vowel:   # not done in exam
        newString += char   # not done in exam
# adding a bool value
flag = False
# checking if there are no vowels in text
if (vowel['a'] == 0 and vowel['e'] == 0 and vowel['i'] == 0 and vowel['o'] == 0 and vowel['u'] == 0):
    flag = True
else:
    flag = False
# check if text field is empty
if text == '':
    print("INVALID INPUT")
# elif not text.isalpha():  # not in exam; check if any numeric value in text; need to add exception for special characters
#    print(0)
elif flag:    # not in exam
    print(0)
else:
    pprint.pprint(vowel)    # not done in exam
    print(newString)
