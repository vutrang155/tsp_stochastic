# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from TSP_recuit import TSPR


class RSD:
    
  # Importation du fichier TSP  et initialisation  INIT
    
    def __init__(self, T0, Tmin, tau, filepath):
        
        # Paramètre algo recuit simule
        self.T0 = T0  # Temperature initiale 
        self.Tmin = Tmin # Temperature finale
        self.tau = tau   # tau : impacte sur la decroissance de la température


        filename = filepath
        m = TSPR(filename+'.tsp')
                
           # Affiche distance entre les villes et le Nombre de villes ( N ) 
           # d : Matrice contenant les distances entre 2 points
           #d[i][j] renvoie la distance entre les points i et j 
        self.N = m.dimension 
        self.d = m.distance_matrix()
        self.x = m.coor_x    # Coordonnees x des villes
        self.y = m.coor_y    # Coordonnees y des villes
                  
        
        
        
        # Trajet initial 
    
        self.ordre_trajet= np.arange(self.N)
        self.init = self.ordre_trajet.copy()

               
        # Trajet en prenant en compte le retour à la ville de départ             
        self.Trajet_optimal=np.append(self.init,self.init[0])
        self.Trajet_init = self.Trajet_optimal
        print(self.Trajet_init)
        
        
        self.Eoptimal = self.Calcul_Energie()   # Energie initiale
        self.Einit = self.Eoptimal
        print("distance initiale ")
        print(self.Einit)
    

    
    # Calcul de l'energie totale correspondant à la distance 
    # totale parcourue par le voyageur 
    def Calcul_Energie(self):
      
        e = 0
        for i in range(0,self.N):
            if i == self.N-1 : #Inclure trajet entre derniere ville et ville départ
                e = e + self.d[self.ordre_trajet[i]][self.ordre_trajet[0]]
            else :
                e = e + self.d[self.ordre_trajet[i]][self.ordre_trajet[i+1]]
            
        return e
    
    
    
    # Simulation d'une fluctuation aleatoire de l'energie du système visant à 
    #atteindre l'equilibre thermique du système pour une temperature donnee
    
    def Fluctuation_systeme(self,j,k):
        Min = min(j,k)
        Max = max(j,k)
        self.ordre_trajet[Min:Max]=self.ordre_trajet[Min:Max].copy()[::-1]
     
    
    
    # Algorithme de Metropolis 
    # Renvoie la nouvelle energie  E2 si E2 >= E1
    # Renvoie E2 avec une probabilté de exp(-dE/T) si E2 < E1 
    def Metropolis(self,E1,E2,j,k,T):
       
        if E1 <= E2:
            E2 = E1 
        else:
            dE = E1 - E2 
            if np.random.uniform() > np.exp(-dE/T):
                self.Fluctuation_systeme(j,k)
            else :
                E2 = E1 
        return E2
    
    
    
    
   
   
    
     # EXECUTION ALGO RECUIT SIMULE
    
    def solve(self):
         
        t =0
        T = self.T0
        
        # initialisation des listes d'historique
        Liste_energie = []     # energie
        Liste_temps = []       # temps
        Liste_T = []           # température
        
        
        
        while T > self.Tmin : 
                # choix de deux villes différentes au hasard
                j = np.random.randint(0,self.N-1)
                k = np.random.randint(0,self.N-1)
            
                if k == j: continue   
            
            # Fluctuation ( equilibre du systeme )
            # Energie calculée 
                self.Fluctuation_systeme(j,k)
                EF = self.Calcul_Energie()
                self.Eoptimal = self.Metropolis(EF,self.Eoptimal,j,k,T)
            
            # Application de la loi de décroissance de la température    
                t += 1
                T = self.T0*np.exp(-t/self.tau)
                
               # historisation des données
                if t % 10 == 0:
                     Liste_energie.append(self.Eoptimal)
                     Liste_temps.append(t)
                     Liste_T.append(T)
                
              
        #Fin de la boucle while      
        
        
        
        
        # Info final trajet - distance
        
        self.Trajet_optimal=np.append(self.ordre_trajet,self.ordre_trajet[0])
        print(self.Trajet_optimal)
        
        
        print("distance optimale ")
        print(self.Eoptimal)
    
        
        
  
        # Affichage des graphes avec trajet initial et trajet optimal
        fig1 = plt.figure(1)
        
        plt.subplot(1,2,1)
        plt.xticks([])
        plt.yticks([])
        plt.plot(self.x[self.init],self.y[self.init],'k')
        # Entre Derniere ville et ville de depart 
        plt.plot([self.x[self.init[-1]], self.x[self.init[0]]],  
                 [self.y[self.init[-1]], self.y[self.init[0]]],'k')
        
        plt.plot(self.x,self.y,'bo')
        plt.plot(self.x[self.init[0]],self.y[self.init[0]],'ro') # point départ rouge
        plt.plot(self.x[self.init[-1]],self.y[self.init[-1]],'go') # point final vert
        plt.title('Trajet initial')
        
        
        
        plt.subplot(1,2,2)
        plt.xticks([])
        plt.yticks([])
        plt.plot(self.x[self.ordre_trajet],self.y[self.ordre_trajet],'k')
        # Entre Derniere ville et ville de depart 
        plt.plot([self.x[self.ordre_trajet[-1]], self.x[self.ordre_trajet[0]]],[self.y[self.ordre_trajet[-1]], self.y[self.ordre_trajet[0]]],'k')
        plt.plot(self.x,self.y,'bo')
        plt.plot(self.x[self.ordre_trajet[0]],self.y[self.ordre_trajet[0]],'ro') # point départ rouge
        plt.plot(self.x[self.ordre_trajet[-1]],self.y[self.ordre_trajet[-1]],'go') # point départ vert
        plt.title('Trajet optimal')
        plt.show()
        
        
        # Affichage de l'evolution de l'energie total du syteme en fonction de t 
        
        plt.subplot(1,2,1)
        plt.semilogy(Liste_temps, Liste_energie)
        plt.title("Evolution de l'energie totale du systeme")
        plt.xlabel('Temps')
        plt.ylabel('Energie')
        
        
        # Affichage de l'evolution de la temperature du syteme en fonction de t 
        
        fig3 = plt.figure(3)
        plt.subplot(1,2,2)
        plt.semilogy(Liste_temps, Liste_T)
        plt.title('Evolution de la temperature du systeme')
        plt.xlabel('Temps')
        plt.ylabel('Temperature')
        plt.show()
            