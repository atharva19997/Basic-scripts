def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)



# join() and split() and partition()
# startswith() and endswith()
# strip() and rstrip() and lstrip()
# ord() and chr()
# >>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
# >>> spam.strip('ampS')
# 'BaconSpamEggs'
# copy() and paste() in pyperclip module