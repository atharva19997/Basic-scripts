import random, sys

print("\nROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0

while True:         # Main Game loop
    print("\n\n%d Wins, %d Losses, %d Ties" % (wins, losses, ties))
    while True:     # Player input loop
        print("Enter yor move: (r)ock, (p)aper, (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            print("\nThank you for playing!")
            sys.exit()
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("\nType ome of 'r', 'p', 's' or 'q'\n")

    # Display player choice
    if playerMove == "r":
        print("\nROCK versus....")
    elif playerMove == "p":
        print("\nPAPER versus....")
    elif playerMove == "s":
        print("\nSCISSORS versus....")

    # Display computer choice
    randomNum = random.randint(1,3)
    if randomNum == 1:
        computerMove = "r"
        print("ROCK\n")
    elif randomNum == 2:
        computerMove = "p"
        print("PAPER\n")
    elif randomNum == 3:
        computerMove = "s"
        print("SCISSOR\n")

    # Display and record wins/losses/ties
    if playerMove == computerMove:
        print("It is a tie!")
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses += 1
