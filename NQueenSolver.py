class NQueenSolver:
    def __init__(self, n):
        self.n = n

    def is_promising(self, s, row):
        return all(row != s[i] and len(s)-i != abs(row-s[i]) for i in range(len(s)))

    def backtracking(self, s):
        if len(s) == self.n: return s
        for row in range(self.n):
            if self.is_promising(s, row):
                found = self.backtracking(s+[row])
                if found != None: return found
        return None

    def solve(self):
        return self.backtracking([])

