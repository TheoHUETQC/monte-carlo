import numpy as np
import matplotlib.pyplot as plt

N = 10**2
N_step = 10**3

#init
x = np.zeros(N_step)
x_final = [] #tableau de resultat

for i in range(N) :
    for n in range(N_step) :
        step = np.random.choice([-1, 1])
        x[n] = x[n-1] + step
    x_final.append(x[n]) #on sauvegarde le resultat
    print(x[n], x[n]*x[n])
x_final = np.array(x_final)

print(np.mean(x_final), " = <x>, doit etre egale a 0 ")
print(np.mean(x_final*x_final), " = <x²>, doit etre egale a", N)
