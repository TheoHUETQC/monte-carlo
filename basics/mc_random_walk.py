import numpy as np
import matplotlib.pyplot as plt

N = 10**2 #nombre de simulation que l on fait pour avoir une moyenne correcte
N_step = 10**3

x_final = [] #tableau de resultat

for i in range(N) :
    x = np.zeros(N_step)
    for n in range(N_step) :
        step = np.random.choice([-1, 1])
        x[n] = x[n-1] + step
    x_final.append(x[n]) #on sauvegarde le resultat
    plt.plot(np.linspace(0, N_step, N_step), x)
    
x_final = np.array(x_final)
average = np.mean(x_final)
variance = np.mean(x_final*x_final)
print(average, " = <x>, doit etre egale a 0 ")
print(variance, " = <x²>, doit etre egale a", N_step)

plt.title(f"Pour {N_step} step, on a  <x²> = {variance}, et <x> = {average}") #  (r"")

plt.show()
