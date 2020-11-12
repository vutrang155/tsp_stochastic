# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:59:07 2020

@author: Rold
"""

import numpy as np
import matplotlib.pyplot as plt
from TSP_recuit import TSP
from Pb_Voyageur_commerce import Recuit_simule


# Parametre algo Recuit simule
# Nom du fichier contenant les données 
 
T0=50.0
Tmin=1e-3
tau=1e4
filename='data16'
traj = Recuit_simule(T0,Tmin,tau,filename)
traj.solve()

