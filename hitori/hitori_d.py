from cell import Cell


class Hitori_d():

    def __init__(self, size, grid):
        self.size = size
        self.grid = grid

    def solve(self):
        r, c = self.select()
        self.grid[r][c].shade = -1
        if self.check_white(r, c):
            if self.isSolved():
                return self.grid
            result = Hitori_d(self.size, self.grid).solve()
            if result:
                return result
        self.grid[r][c].shade = 1
        if self.check_black(r, c):
            if self.isSolved():
                return self.grid
            result = Hitori_d(self.size, self.grid).solve()
            if result:
                return result
        self.grid[r][c].shade = 0
        return False

    def select(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c].shade == 0:
                    return r, c

    def check_white(self, r, c):
        for x in range(self.size):
            if x != c and self.grid[r][x].number == self.grid[r][c].number and self.grid[r][x].shade == -1:
                return False
            if x != r and self.grid[x][c].number == self.grid[r][c].number and self.grid[x][c].shade == -1:
                return False
        return True

    def check_black(self, r, c):
        if r != 0 and self.grid[r-1][c].shade == 1:
            return False
        if r != (self.size - 1) and self.grid[r+1][c].shade == 1:
            return False
        if c != 0 and self.grid[r][c-1].shade == 1:
            return False
        if c != (self.size - 1) and self.grid[r][c+1].shade == 1:
            return False

        ed = 0
        if r == 0 or r == (self.size - 1) or c == 0 or c == (self.size - 1):
            ed += 1
        if r != 0 and c != 0 and self.grid[r-1][c-1].shade == 1:
            ed += self.check_chain(r, c, r, c, r-1, c-1)
            if ed > 1:
                return False
        if r != 0 and c != (self.size-1) and self.grid[r-1][c+1].shade == 1:
            ed += self.check_chain(r, c, r, c, r-1, c+1)
            if ed > 1:
                return False
        if r != (self.size-1) and c != 0 and self.grid[r+1][c-1].shade == 1:
            ed += self.check_chain(r, c, r, c, r+1, c-1)
            if ed > 1:
                return False
        if r != (self.size-1) and c != (self.size-1) and self.grid[r+1][c+1].shade == 1:
            ed += self.check_chain(r, c, r, c, r+1, c+1)
            if ed > 1:
                return False
        return True

    def check_chain(self, rr, cr, rp, cp, rc, cc):
        if rc == rr and cc == cr:
            return 2

        if rc == 0 or cc == 0 or rc == (self.size - 1) or cc == (self.size - 1):
            return 1

        if ((rc-1) != rp or (cc-1) != cp) and self.grid[rc-1][cc-1].shade == 1:
            ed = self.check_chain(rr, cr, rc, cc, rc-1, cc-1)
            if ed > 0:
                return ed
        if ((rc-1) != rp or (cc+1) != cp) and self.grid[rc-1][cc+1].shade == 1:
            ed = self.check_chain(rr, cr, rc, cc, rc-1, cc+1)
            if ed > 0:
                return ed
        if ((rc+1) != rp or (cc-1) != cp) and self.grid[rc+1][cc-1].shade == 1:
            ed = self.check_chain(rr, cr, rc, cc, rc+1, cc-1)
            if ed > 0:
                return ed
        if ((rc+1) != rp or (cc+1) != cp) and self.grid[rc+1][cc+1].shade == 1:
            ed = self.check_chain(rr, cr, rc, cc, rc+1, cc+1)
            if ed > 0:
                return ed

        return 0

    def isSolved(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c].shade == 0:
                    return False
        return True

