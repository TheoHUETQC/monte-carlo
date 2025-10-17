import numpy as np
import matplotlib.pyplot as plt

# OBJECTIF : Approximer pi = 3.1415...

N = 10**3

square_length = 1
r = np.random.rand(N,2)*(square_length) - (square_length/2) #fait des points centré en 0 dans un carré de longueur square_length

plt.figure()
N_cercle = 0
for [x,y] in r :
    plt.scatter(x,y,color = "blue")
    if x**2+y**2 <= square_length**2/4 : #verifie si le point est dans le cercle de diametre square_length
        N_cercle += 1
        plt.scatter(x,y,color = "red")

# air_cercle = pi r²/4 
# or r = 1 et air_carré = 1
# => air_cercle/ air_carré = pi / 4
# donc :
pi = 4* N_cercle/N

print(f"with this method, pi is approximately : {pi}")
print(f"and the error : {np.abs(pi -np.pi)}")
print(f"the expected average error is around : {1/np.sqrt(N)}")

plt.xlim(-square_length/2,square_length/2)
plt.ylim(-square_length/2,square_length/2)
plt.show()
