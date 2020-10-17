import random

randNum = random.randint(1,20)
print("I am thinking of a number between 1 and 20\n\nMake a correct guess in 6 guesses\n")

for guessTaken in range(1,7):
    guess = int(input("Take a guess: "))

    if guess < randNum:
        print("Your guess is too low")
    elif guess > randNum:
        print("Your guess is too high")
    else:
        break

if guess == randNum:
    print("Great! You guessed my number in %d guesses" % guessTaken)
else:
    print("No, my guessed number was " + str(randNum))
