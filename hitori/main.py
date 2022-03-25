from hitori_h import Hitori_h
from hitori_d import Hitori_d
from cell import Cell
import time


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
if alg != 1 and alg != 2:
    print('Input invalid!')
    exit()

print('Demo step by step?')
print('\t1: Yes')
print('\t2: No')
demo = int(input())
if demo == 1:
    demo = True
elif demo == 2:
    demo = False
else:
    print('Input invalid!')
    exit()

ncount = [0]

if alg == 1:
    hitori = Hitori_d(size, grid, ncount, demo)
elif alg == 2:
    hitori = Hitori_h(size, grid, ncount, demo)



print('Solving...')

tr = time.time()

result = hitori.solve()

tr = time.time() - tr
if result:
    print('Solved!') 
    for r in range(size):
        for c in range(size):
            print(result[r][c].shade, end=' ')
        print()
else:
    print('Can\'t solve this game :((')
    
if not demo:
    print("Time run:", tr)
    print("Node count:", ncount[0])