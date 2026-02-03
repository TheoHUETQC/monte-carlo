import matplotlib.pyplot as plt
import numpy as np

def variance(x : np.array) -> float:
  mean_x = np.mean(x)
  mean_x2 = np.mean(x*x)
  return mean_x2 - mean_x**2

def time_averaged_values(y : list) -> list :
  y_average = []
  N = len(y)
  T = N//10
  for n in range(N) :
    if n < T :
       R = n 
    elif n + T > N :
       R = N - n 
    else :
       R = T
    y_average.append(np.mean(y[n - R: n + R]))
  return y_average

def plot2(x : list, y1 : list, y2 : list, y1_theoric : list =[], y2_theoric : list =[], show_y1_average : bool = False, show_y2_average : bool = False, title1 : str ="plot 1", title2 : str ="plot 2", x_label : str = "x", Tt : list = []) -> None :
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax = [ax1, ax2]
    y = [y1, y2]
    y_theoric = [y1_theoric, y2_theoric]
    title = [title1, title2]
    show_average = [show_y1_average, show_y2_average]

    for i in range(2) :
        ax[i].plot(x, y[i], color='blue',label='numeric result')
        if len(y_theoric[i]) != 0 :
            ax[i].plot(x, y_theoric[i], color='red', label='theoric result')
        if show_average[i] :
            ax[i].plot(x, time_averaged_values(y[i]), color='orange',label='numeric average')
        ax[i].set_title(title[i])
        ax[i].set_ylabel(title[i])
        ax[i].set_xlim(x[0], x[-1])
        ax[i].legend()
        ax[i].set_xlabel(x_label)
        ax[i].grid()
        for Ti in Tt :
            ax[i].axvline(x=Ti,color='green',linestyle='--', alpha = 0.2)

    plt.tight_layout()
    plt.show()

"""
    previous_Tn = n-T//2 if n-T//2 > 0 else 0
    next_Tn = n+T//2 if n+T//2 < N else N"""
    
