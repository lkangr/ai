from cell import Cell
from sudoku_h import Sudoku_h
from sudoku_d import Sudoku_d

print("Select input: ", end='')
ip = input()

try:
    with open('input/'+ip+'.txt') as f:
        grid = []
        line = f.readline()
        while(line):
            grid += [list(map(lambda x: Cell(int(x)), line.split()))]
            line = f.readline()
except:
    print('Can\'t open input file.')
    exit()


print('Select algorithm:')
print('\t1: Depth first search')
print('\t2: Heuristic')
alg = int(input())

if alg == 1:
    sudoku = Sudoku_d(grid)
elif alg == 2:
    sudoku = Sudoku_h(grid, True)
else:
    print('Input invalid!')
    exit()



print('Solving...')

result = sudoku.solve()
if result:
    print('Solved!') 
    for r in range(9):
        for c in range(9):
            print(result[r][c].number, end=' ')
        print()
else:
    print('Can\'t solve this game :((')