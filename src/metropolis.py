import numpy as np
import matplotlib.pyplot as plt

N = 10**3

def p(x) :
    return np.exp(x**2/2)

alpha = 1

x = np.zeros(N)

for n in range(N) :
    delta = np.random.uniform(- alpha, alpha)
    x_proposal = x[n-1] + delta 
    A = p(x_proposal)/p(x[n-1])
    P_accepté = min(1,A)
    if np.random.rand() < P_accepté :
        x[n] = x[n-1] + delta
    else :
        x[n] = x[n-1]

plt.plot(np.linspace(0, N, N), x)
plt.show()