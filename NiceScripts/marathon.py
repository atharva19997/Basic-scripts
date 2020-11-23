import sys

R = []
print("Enter the distances covered by athlets in Marathon (Kilometers) please")
print("(press q to terminate)")

while True:
    get = input()
#    try:
       # if float(get) <= 0:
        #    print("Invalid Input!")
         #   sys.exit()
#    except ValueError:
#        break
    if str(get) == 'q':
        break
    R += [float(get)]
    
if any(num < 0 for num in R):
    print("Invalid Input!")
    sys.exit()

R.remove(42.195)
R.remove(0)
R.sort(reverse = True)

print("Highest Distances covered excluding Finishers:")
print(R[0],R[1],R[2])
