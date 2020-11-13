from TSP import TSP
import numpy as np
import matplotlib.pyplot as plt
from solver.PS import PS
import time

def plot_tour(dat, index_list, p=plt):
    for k in range((index_list).shape[0]):
        if k == (index_list).shape[0] - 1:
            x1 = [dat[index_list[k], 0], dat[index_list[0], 0]]
            x2 = [dat[index_list[k], 1], dat[index_list[0], 1]]
            p.plot(x1, x2, 'k')
        else:
            x1 = [dat[index_list[k], 0], dat[index_list[k + 1], 0]]
            x2 = [dat[index_list[k], 1], dat[index_list[k + 1], 1]]
            p.plot(x1, x2, 'k')

if __name__ == '__main__':
    # Initialisation
    filename = 'berlin52'
    m = TSP('data/'+filename+'.tsp')
    a = 0.8
    t = 0.2

    t0 = time.time()
    sd = PS(m)
    (dist_d, x_d, u_d) = sd.solve()
    t1 = time.time()
    total = t1-t0
    print("Résourdre TSP déterministe en {0:.1f}s, \n\tfonction objectif = {1:.2f}"\
          .format(total, dist_d))

    t0_ = time.time()
    ss = PS(m, mod="stochastic", alpha=a, taux_majoration=t)
    (dist_s, x_s, u_s) = ss.solve()
    t1_ = time.time()
    total_ = t1_-t0_
    print("Résourdre TSP stochastique en {0:.1f}s, \
          \n\talpha={1:.1f}, taux_majoration={2:.1f}\
          \n\tfonction objectif = {3:.2f}" \
          .format(total_, a, t, dist_s))


    m_np = np.reshape(np.array(m.positions), (-1, 2))
    x = np.reshape(m_np[:, 0], (-1, 1))
    y = np.reshape(m_np[:, 1], (-1, 1))

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle("TSP")
    ax1.set_title("Solution Déterministe d={0:.2f}".format(dist_d))
    ax2.set_title("Solution Stochastique d={0:.2f} (a={1}%,t={2}%)".format(dist_s, (a*100), (t*100)))
    ax1.get_xaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)
    ax2.get_xaxis().set_visible(False)
    ax2.get_yaxis().set_visible(False)
    # Place points
    ax1.plot(x, y, 'bo')
    ax2.plot(x, y, 'bo')

    g_d = np.argsort(u_d, axis=0)
    plot_tour(m_np, g_d, ax1)

    g_s = np.argsort(u_s, axis=0)
    plot_tour(m_np, g_s, ax2)
    plt.savefig('g.png')
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
