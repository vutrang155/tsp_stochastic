import numpy as np
import random
import math
from scipy.stats import norm

from docplex.mp.model import Model

from TSP import TSP

# Ignore RuntimeWarning
import warnings
warnings.filterwarnings("ignore",category =RuntimeWarning)

class PS:
    def __init__(self, tsp_dat, mod='determinist', alpha=None, taux_majoration=None):
        self.data = tsp_dat
        self.mod = mod
        self.model = Model(name="TSP " + self.mod)
        self.alpha = alpha
        self.taux_majoration = taux_majoration
        # Throw exception if alpha and taux_marjoration = null if it's a stochastic model
        if mod == "stochastic" and (self.alpha == None or self.taux_majoration == None):
            raise ValueError("Stochastic model must have alpha and taux_majoration")

        self.init_model()

    # return distance, x, u
    def solve(self):
        n = self.data.dimension
        sol = self.model.solve()
        x = np.zeros((n, n))
        u = np.zeros((n, 1))

        # Get x
        for i in range(n):
            for j in range(n):
                x[i, j] = sol.get_value('x_{0}_{1}'.format(i, j))

        # Get y
        for i in range(n):
            u[i] = sol.get_value('u_{0}'.format(i))

        return (sol.objective_value, x, u)

    def init_model(self):
        n = self.data.dimension
        c = self.data.distance_matrix()
        x = {(i, j): self.model.binary_var(name='x_{0}_{1}'.format(i, j)) for i in range(n) for j in range(n)}
        u = {i: self.model.integer_var(name='u_{0}'.format(i), lb=1, ub=n - 1) for i in range(n)}

        # Objective function:
        tsp_func = self.model.sum(c[i, j] * x[(i, j)] for i in range(n) for j in range(n))
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
                if i != j:
                    self.model.add_constraint(u[i] - u[j] + n * x[(i, j)] <= n - 1)
        for i in range(1,n):
            self.model.add_constraint(u[i] <= n - 1)
            self.model.add_constraint(u[i] >= 1)
        # Constraint 1d: stochastic constraint
        if self.mod == "stochastic":
            (Z,_,_) = PS(self.data).solve()
            # Generate variance
            variances = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    if i > j:
                        variances[i, j] = c[i, j] * random.random()
                        variances[j, i] = variances[i, j]

            for i in range(n):
                for j in range(n):
                    quantile = norm.ppf(self.alpha, loc=c[i, j], scale=math.sqrt(variances[i, j]))
                    self.model.add_constraint(x[(i, j)]*(c[i, j] + math.sqrt(variances[i, j])*quantile) <= Z)