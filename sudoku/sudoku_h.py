from copy import deepcopy
from cell import Cell


class Sudoku_h():

    def __init__(self, grid, first):
        self.grid = grid
        self.first = first

    def solve(self):
        if self.first:
            self.set_hypo()
        t = self.fill_grid()
        while t != 0:
            if t == -1:
                return False
            t = self.fill_grid()
        if self.isSolved():
            return self.grid
        r, c = self.select_hypo()
        for x in self.grid[r][c].hypo:
            self.hypo_grid = deepcopy(self.grid)
            self.hypo_grid[r][c].number = x
            self.del_h(x, r, c)
            result = Sudoku_h(self.hypo_grid, False).solve()
            if result:
                return result
        return False

    def set_hypo(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c].number != 0:
                    continue
                for x in range(1, 10):
                    if not self.check_exist(x, r, c):
                        self.grid[r][c].hypo += [x]

    def check_exist(self, x, r, c):
        for z in range(9):
            if self.grid[z][c].number == x or self.grid[r][z].number == x:
                return True
        for m in self.get_region(r):
            for n in self.get_region(c):
                if self.grid[m][n].number == x:
                    return True
        return False

    def get_region(self, d):
        if d < 3:
            return range(3)
        elif d < 6:
            return range(3, 6)
        else:
            return range(6, 9)

    def fill_grid(self):
        b = 0
        for r in range(9):
            for c in range(9):
                if self.grid[r][c].number != 0:
                    continue
                for x in self.grid[r][c].hypo:
                    if self.check_hypo(x, r, c):
                        self.grid[r][c].number = x
                        self.del_hypo(x, r, c)
                        b = 1
                        if not self.check_grid(r, c):
                            return -1
                        break
        return b

    def check_hypo(self, x, r, c):
        b = True
        for z in range(9):
            if z != r and self.grid[z][c].number == 0 and x in self.grid[z][c].hypo:
                b = False
                break
        if b:
            return True
        b = True
        for z in range(9):
            if z != c and self.grid[r][z].number == 0 and x in self.grid[r][z].hypo:
                b = False
                break
        if b:
            return True
        for m in self.get_region(r):
            for n in self.get_region(c):
                if (m != r or n != c) and self.grid[m][n].number == 0 and x in self.grid[m][n].hypo:
                    return False
        return True

    def del_hypo(self, x, r, c):
        for z in range(9):
            if x in self.grid[z][c].hypo:
                self.grid[z][c].hypo.remove(x)
            if x in self.grid[r][z].hypo:
                self.grid[r][z].hypo.remove(x)
        for m in self.get_region(r):
            for n in self.get_region(c):
                if x in self.grid[m][n].hypo:
                    self.grid[m][n].hypo.remove(x)

    def check_grid(self, r, c):
        for z in range(9):
            if z != r and self.grid[z][c].number == self.grid[r][c].number:
                return False
            if z != c and self.grid[r][z].number == self.grid[r][c].number:
                return False
        for m in self.get_region(r):
            for n in self.get_region(c):
                if (m != r or n != c) and self.grid[m][n].number == self.grid[r][c].number:
                    return False
        return True

    def del_h(self, x, r, c):
        for z in range(9):
            if x in self.hypo_grid[z][c].hypo:
                self.hypo_grid[z][c].hypo.remove(x)
            if x in self.hypo_grid[r][z].hypo:
                self.hypo_grid[r][z].hypo.remove(x)
        for m in self.get_region(r):
            for n in self.get_region(c):
                if x in self.hypo_grid[m][n].hypo:
                    self.hypo_grid[m][n].hypo.remove(x)

    def isSolved(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c].number == 0:
                    return False
        return True

    def select_hypo(self):
        x = 10
        for r in range(9):
            for c in range(9):
                if self.grid[r][c].number == 0 and len(self.grid[r][c].hypo) < x:
                    x = len(self.grid[r][c].hypo)
                    ro = r
                    co = c
        return ro, co

