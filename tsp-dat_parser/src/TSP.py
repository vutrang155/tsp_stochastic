import numpy as np


class TSP:
    def __init__(self, filepath):
        infile = open(filepath, 'r')

        self.name = infile.readline().strip().split()[1]  # NAME
        self.fileType = infile.readline().strip().split()[1]  # TYPE
        self.comment = infile.readline().strip().split()[1]  # COMMENT
        self.dimension = int(infile.readline().strip().split()[1])  # DIMENSION
        self.edgeWeightType = infile.readline().strip().split()[1]  # EDGE_WEIGHT_TYPE
        infile.readline()

        self.positions = []
        if self.edgeWeightType == "EUC_2D":
            for i in range(self.dimension):
                x, y = infile.readline().strip().split()[1:]
                self.positions.append([float(x), float(y)])

    def dist(self, i, j):
        a = np.array(self.positions[i])
        b = np.array(self.positions[j])
        return np.linalg.norm(a - b)

    def distance_matrix(self):
        n = self.dimension
        ret = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                ret[i, j] = self.dist(i, j)
        return ret
