def TtoB():
    binTerm = []
    term = input("Input a text to convert to binary (eg: Hello world):\n")
    for char in term:
        binTerm.append(bin(ord(char)))
    for i in binTerm: print(i[2:], " ", end="")
    print("\n")

def BtoT():
    term  = input("Input a binary to convert to text (eg: 0b10100101 so on OR 10011101 so on):\n")
    for num in term.split():
        try:
            if num.isnumeric():
                letter = chr(int(num, 2))
            else:
                letter = chr(int(num[2:], 2))
            print(letter, end="")
        except ValueError: print(" *Wrong Input* ", end="")
    print("\n")

while True:
    convert = input("""Input '1' to convert text to binary
Input '2' to convert binary to text
Input 'e' to exit\n""")
    if convert == '1': TtoB()
    elif convert == '2': BtoT()
    elif convert == 'e': break
    else: print("Input only 1 or 2 or e\n")
