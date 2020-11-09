
import numpy as np
import matplotlib.pyplot as plt
from TSP_recuit import TSP
from Pb_Voyageur_commerce import Recuit_simule


# Parametre algo Recuit simule
# Nom du fichier contenant les données 
 
T0=22.0
Tmin=1e-2
tau=1e4
filename='rold_test'
traj = Recuit_simule(T0,Tmin,tau,filename)
traj.run()

