#Collatz Sequence

while True:
    try:
        number = int(input("Enter a number:\n"))
        if number <= 0:
            print("Please enter a Natural number(That was NOT natural)")
            continue
        else:
            break
    except ValueError:
        print("Please enter a Natural number")
    continue

def collatz(number1):
    remain = number1 % 2
    if remain == 0:
        number1 = (number1 // 2)
        return number1
    else:
        number1 = (3 * number1 + 1)
        return number1

while True:
    number = collatz(number)
    if number != 1:
        print(number)
    else:
        print(1)
        break
