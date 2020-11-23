# only made for Maitreyee and Tanistha.
regPass = 0
while True:
    print("+ "*10 +"Register on Facebook" + " +"*10 + "\n")
    regName = input("Your Name: ")
    regAge = int(input("Your Age: "))
    if regAge < 18:
        print("You are not allowed to be on Facebook! Please come back when you are 18 or more.\n \n")
        continue
    else:
        regPass = input("Please input new Password:\n")
        break
print(" \n" * 2 + "+ "*10 + "Welcome to Facebook" + " +"*10 + "\n")
while True:
    name = input("Please enter registered Name: ")
    if name == regName:
        print("\nHello " + name + "\n")
    else:
        print("\nWe do not Know you, please register then login\n")
        continue
    while True:
        password = input("Please enter Password: ")
        if password == regPass:
            print("\nPassword Correct")
            break
        else:
            print("\nWrong password")
            continue
    break
print("\n" * 5)
print("*" * 70)
print("Facebook crashed because a DUMB person just logged in.")
print("We have removed his/her account so he/she would not login again.")
print("Sorry for inconvenience and Thank you for your cooperation.")
print("*" * 70 + "\n")
