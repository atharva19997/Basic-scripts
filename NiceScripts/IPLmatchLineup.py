from itertools import combinations

teams = []
team = ''
while team != 'Q':
    team = input()
    teams += [team]
teams.remove('Q')    # didnt do it in exam
#print(teams)

matches = ((len(teams) * (len(teams) - 1)) / 2)
print("\nNUMBER OF MATCHES: ", int(matches))

comb = combinations(teams, 2) # awesome library tool
for i,j in comb:
    print(i + "-VS-" + j)
print()