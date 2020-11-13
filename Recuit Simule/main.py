# -*- coding: utf-8 -*-



from RSD import RSD


# Parametre algo Recuit simule
# Nom du fichier contenant les données 
 
T0=50.0
Tmin=1e-3
tau=1e4
filename='berlin52'
traj = RSD(T0,Tmin,tau,filename)
traj.solve()

