from NQueenSolver import NQueenSolver

for n in range(1, 9):
    print("Solución con %d reinas: %s" % (n, NQueenSolver(n).solve()))