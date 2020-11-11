import solver.SolverTSP
from TSP import TSP

from docplex.mp.model import Model

class PS:
    def __init__(self, tsp_dat):
        self.data = tsp_dat
        self.model = Model(name="TSP deterministic")
        self.init_model()

    def solve(self):
        return self.model.solve()
    def init_model(self):
        n = self.data.dimension
        D = self.data.distance_matrix()
        x = {(i, j): self.model.binary_var(name='x_{0}_{1}'.format(i, j)) for i in range(n) for j in range(n)}
        u = {i: self.model.integer_var(name='u_{0}'.format(i), lb=1, ub=n-1) for i in range(n)}

        # Objective function:
        tsp_func = self.model.sum(D[i, j]*x[(i, j)] for i in range(n) for j in range(n))
        self.model.minimize(tsp_func)

        # Constraint function:
        # Constraint to eliminate condition i!j in 1a and 1b:
        for i in range(n):
            self.model.add_constraint(x[(i, i)] == 0)
        # Constraint 1a:
        for i in range(n):
            self.model.add_constraint(self.model.sum(x[(i, j)] for j in range(n)) == 1)
        # Constraint 1b:
        for j in range(n):
            self.model.add_constraint(self.model.sum(x[(i, j)] for i in range(n)) == 1)

        # Constraint 1c: Subtour elimination
        for i in range(1, n):
            for j in range(1, n):
                self.model.add_constraint(u[i] - u[j] + n*x[(i, j)] <= n - 1)

if __name__ == "__main__":
    filename = 'berlin52'
    m = TSP(filename+'.tsp')

    # Generate distance matrix
    n = m.dimension
    D = m.distance_matrix()

    solveur = PS(m)
    sol = solveur.solve()
