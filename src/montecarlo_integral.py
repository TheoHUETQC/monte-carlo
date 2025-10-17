import numpy as np
import matplotlib.pyplot as plt

# OBJECTIF : Approximer l'integrale de f(x) sur [a,b]

N = 10**5
a, b = 0, 1

def f(x) : 
    return x**2

x = np.random.rand(N,1) * (b - a) + a #genere des points entre a et b

integral = (b-a)/N * np.sum(f(x))

print(integral)
