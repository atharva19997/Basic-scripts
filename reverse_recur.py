def reverse_recur(str):
    if len(str) == 0:
        return str
    else:
        return reverse_recur(str[1:]) + str[0]
 
str = input("Enter your string: ")
rev_str = reverse_recur(str)
print ('Reverse of your string: ', rev_str)
