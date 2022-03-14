from cell import Cell


class Sudoku_d():

    def __init__(self, grid):
        self.grid = grid


    def solve(self):
        r, c = self.select_cell()
        for x in range(1, 10):
            self.grid[r][c].number = x
            if not self.check_grid(r, c):
                continue
            if self.isSolved():
                return self.grid
            result = Sudoku_d(self.grid).solve()
            if result:
                return result
        self.grid[r][c].number = 0
        return False


    def select_cell(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c].number == 0:
                    return r, c

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


    def get_region(self, d):
        if d < 3:
            return range(3)
        elif d < 6:
            return range(3, 6)
        else:
            return range(6, 9)


    def isSolved(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c].number == 0:
                    return False
        return True