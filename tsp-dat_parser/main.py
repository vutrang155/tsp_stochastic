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
    x=np.reshape(m_np[:,0],(-1,1))
    y=np.reshape(m_np[:,1],(-1,1))
    plt.plot(x ,y,'bo')
    for i in range(len(x)):
        plt.text(x[i], y[i], str(i))

    sol=[0,
     9,
     4,
     30,
     27,
     29,
     8,
     46,
     45,
     44,
     40,
     32,
     37,
     38,
     28,
     15,
     5,
     3,
     48,
     12,
     6,
     1,
     11,
     26,
     31,
     35,
     34,
     33,
     14,
     10,
     2,
     50,
     42,
     18,
     19,
     20,
     23,
     24,
     21,
     22,
     47,
     7,
     43,
     17,
     49,
     16,
     36,
     25,
     51,
     13,
     41,
     39]
    sol=np.argsort(sol)
    print(sol)
    for k in range((sol).shape[0]):
        if k == (sol).shape[0]-1:
            x1 = [m_np[sol[k],0], m_np[sol[0],0]]
            x2 = [m_np[sol[k],1], m_np[sol[0],1]]
            plt.plot(x1,x2)
        else:
            x1 = [m_np[sol[k],0], m_np[sol[k+1],0]]
            x2 = [m_np[sol[k],1], m_np[sol[k+1],1]]
            plt.plot(x1, x2)
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
