import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad #pour avoir la valeur exacte de l'integrale que l'on approxime

# OBJECTIF : Approximer l'integrale de f(x) sur [a,b] avec Deux methodes 

N = 10**6

def f(x) : 
    return np.exp(-x)*x**2

# intégration par échantillonnage uniforme (a et b sont fini) :

a, b = 0, 1

x = np.random.uniform(a,b,N) #genere N points aléatoire entre a et b
fx = f(x)

average = np.mean(fx) #  = np.sum(f(x))/N = moyenne des f(xi)
integral = (b-a) * average

I_exact, _ = quad(f, a, b)

print("integration by uniform sampling :")
print(f"with this method, the integral is approximately : {integral}")
print(f"and the error : {np.abs(integral - I_exact)}")
print(f"the expected average error is around : {(b - a) * np.std(fx)/np.sqrt(N)}")

print()

# Importance Sampling (quelque soit a et b) ici de 0 à +∞:

"""
Integrale I = ∫ f(x) dx
            = ∫ f(x)*p(x)/p(x) dx
            = 1/N ∑f(xi)/p(xi) 
où p(x) est une densité proche de la forme de f(x)
"""
def p(x) : #on choisis p une **densité** de la forme la plus similaire a f (le plus optimal p(x)= ∣f(x)∣ / ∫∣f(x′)∣dx′ mais cela depend de l integrale que l'on veut calculer donc pas possible a avoir​)
    return np.exp(-x) #ici f(x) ∝ exp(-x)

def p_invers(x) : # fonction tel que : p_invers(p(x)) = x
    return - np.log(u) 

u = np.random.uniform(0,1,N)  # genere N points aléatoire entre 0 et 1
x = p_invers(u)               # on transforme via l inverse de p(x) nos valeur de 0 a +∞

f_p = f(x)/p(x)
integral = np.mean(f_p) # = np.sum(f(x)/p(x))/N 
I_exact = 2 # ∫₀^∞ x^n e^{-x} dx = n!

print("Importance Sampling :")
print(f"with this method, the integral is approximately : {integral}")
print(f"and the error : {np.abs(integral - I_exact)}")
print(f"the expected average error is around : {np.std(f_p) / np.sqrt(N)}")
