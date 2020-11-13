# -*- coding: utf-8 -*-


import numpy as np

class TSPR:
    
    def __init__(self, filepath):
        infile = open(filepath, 'r')

        name = infile.readline()  # NAME
        fileType = infile.readline()  # TYPE
        comment = infile.readline() # COMMENT
       
        # DIMENSION
        dim = infile.readline().strip().split()
        if(len(dim) == 2):
            self.dimension = int(dim[1]) 
        elif(len(dim) == 3) :
            self.dimension = int(dim[2]) 
            
        
        # EDGE_WEIGHT_TYPE
        eweighttype = infile.readline().strip().split()
        if(len(eweighttype) == 2):
            self.edgeWeightType = eweighttype[1]
        elif(len(eweighttype) == 3) :
            self.edgeWeightType = eweighttype[2]
            
            
        infile.readline()

        self.positions = np.zeros((self.dimension,2)) 
        self.coor_x = np.zeros(self.dimension)
        self.coor_y = np.zeros(self.dimension) 


        if self.edgeWeightType == "EUC_2D":
            for i in range(self.dimension):
                x, y = infile.readline().strip().split()[1:]
              
                self.positions[i][0]=float(x)
                self.positions[i][1]=float(y)  
                self.coor_x[i]=float(x) 
                self.coor_y[i]=float(y) 


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