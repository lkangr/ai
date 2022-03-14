from hitori_h import Hitori_h
from hitori_d import Hitori_d
from cell import Cell


print("Select input: ", end='')
ip = input()

try:
    with open('input/'+ip+'.txt') as f:
        size = int(f.readline())
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
    hitori = Hitori_d(size, grid)
elif alg == 2:
    hitori = Hitori_h(size, grid)
else:
    print('Input invalid!')
    exit()



print('Solving...')

result = hitori.solve()
if result:
    print('Solved!') 
    for r in range(size):
        for c in range(size):
            print('{: }'.format(result[r][c].shade), end=' ')
        print()
else:
    print('Can\'t solve this game :((')