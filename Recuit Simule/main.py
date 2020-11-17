# -*- coding: utf-8 -*-



from RSD import RSD
from RSS import RSS
import time

# Parametre algo Recuit simule
# Nom du fichier contenant les données 

if __name__ == "__main__":
    T0=50.0
    Tmin=1e-3
    tau=1e4
    filename='Data/berlin52'

    t0 = time.time()

    traj = RSD(T0,Tmin,tau,filename)
    traj.solve()

    t1 = time.time()
    total = t1-t0
    print("Resourdre RSD en {0:.1f}s ".format(total))

    t0 = time.time()

    traj = RSS(T0,Tmin,tau,filename)
    traj.solve()

    t1 = time.time()
    total = t1-t0
    print("Resourdre RSS en {0:.1f}s ".format(total))

