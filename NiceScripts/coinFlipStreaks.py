# not original :(
import random
def flip():
    flipvalue = random.randint(1,2)
    if flipvalue == 1:
        side = "Heads"
    else:
        side = "Tails"
    return side

def nStreak():
    numFlips = int(input("Number of Flips: "))
    lengthStreak = int(input("Length of streak: "))
    numRuns, heads, tails, numStreakHeads, numStreakTails = 0, 0, 0, 0, 0

    while numRuns != numFlips:
        side = flip()
        numRuns += 1
        if side == "Heads":
            heads += 1
            tails = 0
            if heads == lengthStreak:
                numStreakHeads += 1
                heads = 0
        if side == "Tails":
            tails += 1
            heads = 0
            if tails == lengthStreak:
                numStreakTails += 1
                tails = 0
    print("Number of Head Streaks: ", numStreakHeads)
    print("Number of Head Streaks: ", numStreakTails)
nStreak()