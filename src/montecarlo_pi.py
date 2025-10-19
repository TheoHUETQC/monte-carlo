import numpy as np
import matplotlib.pyplot as plt

# OBJECTIF : Approximer π ≃ 3.1415...

N = 10**5
PLOT_GRAPH = False

L = 1 # taille du carré
R = L # rayon du cercle

#Genere nos points aléatoire dans le carré
r = np.random.rand(N,2)*(L) #fait des points dans un carré de longueur L

#compte le nombre de point dans le cercle de rayon R
N_cercle = np.count_nonzero(np.linalg.norm(r, axis = 1) <= R) 
N_carre = N #tout les points sont dans le carré

"""
air_cercle = pi R²/4 
air_carré  = L²
=> air_cercle/ air_carré = (pi * R²) / (4 * L²)
donc :
"""
pi = (4* L**2 * N_cercle)/(N_carre * R**2)

print(f"with this method, pi is approximately : {pi}")
print(f"and the error : {np.abs(pi -np.pi)}")
print(f"the expected average error is around : {1/np.sqrt(N)}")

#figure montre où sont les points
if PLOT_GRAPH :
    plt.figure()
    for [x,y] in r :
        plt.scatter(x,y,color = "blue")
        if x**2+y**2 <= R**2 : #verifie si le point est dans le cercle de rayon R
            plt.scatter(x,y,color = "red")
    plt.xlim(0,L)
    plt.ylim(0,L)
    plt.title(f"Distrubtion de {N} points aléatoires, rouge = dans le cercle de rayon {R} \n Ici π ≃ {pi}")
    plt.show()
