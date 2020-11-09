# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:47:39 2020

@author: Rold
"""
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

        self.positions = np.zeros((self.dimension,2)) #MODIFY
        self.coor_x = np.zeros(self.dimension) # ADD
        self.coor_y = np.zeros(self.dimension) # ADD


        if self.edgeWeightType == "EUC_2D":
            for i in range(self.dimension):
                x, y = infile.readline().strip().split()[1:]
              
                self.positions[i][0]=float(x)  #MODIFY
                self.positions[i][1]=float(y)  #MODIFY
                self.coor_x[i]=float(x) # ADD
                self.coor_y[i]=float(y) # ADD


    def dist(self, i, j):
        a = np.array(self.positions[i])
        b = np.array(self.positions[j])
        return np.linalg.norm(a - b)

    def distance_matrix(self):
        n = self.dimension
        D = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                D[i, j] = self.dist(i, j)
        return D