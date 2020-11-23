tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

# not original :(
def printTable(table):
    colWidth = [0] * len(table)

    for y in range(len(table)):
        for x in table[y]:
            if colWidth[y] < len(x):
                colWidth[y] = len(x)
    
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidth[y]), end = ' ')
        print()
        x += 1

printTable(tableData)