spam = []
print("Enter List items please(press 'q' to view list)")
while True:
    get = input()
    if get == 'q':
        break
    elif get == '':
        print("Put an item please or press 'q' to view list")
        continue
    spam += [get]

last = spam[-1]

print("The list is : ", end = '')
for item in spam[:-1]:
    print(item + ", ", end = '')

if len(spam) == 1:
    print(last + ".")
else:
    print("and " +last + ".")
