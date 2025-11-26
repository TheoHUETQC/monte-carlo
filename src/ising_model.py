import matplotlib.pyplot as plt
import numpy as np

def init_lattice(l) :
    lattice = (2*np.random.randint(0,2,size=(l,l))-1)
    return lattice

def deltaE(i,j) :
    SD = lattice[(i - 1) % l, j] + lattice[(i + 1) % l, j] + \
          lattice[i, (j - 1) % l] + lattice[i, (j + 1) % l] 
    return 2*J*lattice[i,j]*SD

def move() :
    i,j = np.random.randint(l), np.random.randint(l)
    dE = deltaE(i, j)
    if dE < 0 :
        lattice[i, j] = -lattice[i, j]
        return
    if np.random.random() < np.exp(-dE*beta) :
        lattice[i, j] = -lattice[i, j]
        return 
    return

def magnetization(lattice) :
    return np.sum(lattice)/float(l*l)

# --- paramètres globaux ---
global lattice, J, beta, l
J = 1
l = 20
n = l * l
K = 3

# liste des températures
T_low  = np.linspace(1.5, 1.99, 10)    # bas T
T_crit = np.linspace(2.00, 2.6, 80)    # dense autour de Tc
T_high = np.linspace(2.61, 3.5, 11)    # haut T
T_list = np.concatenate([T_low, T_crit, T_high])

# tableau pour magnétisation moyenne
mag = np.zeros(len(T_list))

# tableau pour susceptibilité
mag2 = np.zeros(len(T_list))
X = np.zeros(len(T_list))

indice = 0
for T in T_list :
    beta = 1./T
    
    lattice = init_lattice(l)

    #   THERMALISATION
    for t in range(0,1000) :
        for mc in range(0,n) :
            move()
    print("thermalization finished for T =", T)

    #  MESURES STATISTIQUES
    for t in range(0,200) :
        for mc in range(0, n*K):
            move()

        m = abs(magnetization(lattice))
        mag[indice] += m
        mag2[indice] += m*m

    mag[indice] /= 200
    mag2[indice] /= 200

    # susceptibilité χ = ( <m²> – <m>² ) * beta
    X[indice] = (mag2[indice] - mag[indice]*mag[indice]) * beta

    # VISUALISATION 1 fois sur 50
    if indice % 50 == 0 :
        plt.matshow(lattice)
        plt.xlabel("i")
        plt.ylabel("j")
        plt.title("Ising 2D -- Configuration à T = "+str(round(T,3)))
        plt.xlim(0,l)
        plt.ylim(0,l)
        plt.savefig("Ising2d_config_T"+str(round(T,3))+".png")
        plt.show()

    indice += 1

# COURBE MAGNÉTISATION
plt.plot(T_list, mag, marker='o')
plt.xlabel("T")
plt.ylabel("<m>")
plt.title("Ising 2D -- Magnétisation <m>(T)")
plt.xlim(T_list[0], T_list[-1])
plt.ylim(0., 1.)
plt.grid()
plt.savefig('Ising2d_L20_magnetization_curve.png')
plt.show()

# COURBE SUSCEPTIBILITÉ
plt.plot(T_list, X, marker='o')
plt.xlabel("T")
plt.ylabel("χ(T)")
plt.title("Ising 2D -- Susceptibilité χ(T)")
plt.xlim(T_list[0], T_list[-1])
plt.ylim(0., max(X)*1.2)
plt.grid()
plt.savefig('Ising2d_L20_susceptibility_curve.png')
plt.show()