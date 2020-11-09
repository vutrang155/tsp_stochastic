from TSP import TSP
import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
    filename = 'berlin52'
    m = TSP(filename+'.tsp')

    # Generate distance matrix
    n = m.dimension
    D = m.distance_matrix()

    m_np = np.reshape(np.array(m.positions), (-1, 2))
    x = m_np[:,0]
    y = m_np[:,1]
    print(x)
    plt.plot(x ,y,'bo')

    sol = [1,22,31,18,3,17,21,42,7,2,30,23,20,50,29,16,46,44,34,35,36,39,40,37,38,48,24]
    sol = list(map(lambda x : x-1, sol))
    print(sol)
    for i in sol:
        plt.plot(m_np[i,0], m_np[i,1], 'r-')
    plt.show()

'''
    # Write to dat
    f = open(filename+".dat", "w")
    f.write("n = "+str(n)+";\n")
    f.write("C = [")
    for i in range(n):
        f.write("[")
        for j in range(n):
            f.write(str(D[i, j]))
            if j != n-1:
                f.write(",")
        f.write("]")
        if i != n-1:
            f.write(",\n\t")
    f.write("];")
    f.close()
    '''
