import matplotlib.pyplot as plt
import numpy as np

def time_averaged_values(y : list) -> list :
  y_average = []
  N = len(y)
  T = N//20
  for n in range(N) :
    if n == 0 :
      y_average_temp = y[0]
    elif n == N-1:
      y_average_temp = y[-1]
    else :
      if n < T :
        R = n
      elif n + T > N :
        R = N - n
      else :
        R = T
      y_average_temp = np.mean(y[n - R: n + R])
    y_average.append(y_average_temp)
  return y_average

def plot2(x : list, y1 : list, y2 : list, y1_theoric : list =[], y2_theoric : list =[], show_y1_average : bool = False, show_y2_average : bool = False, title1 : str ="plot 1", title2 : str ="plot 2", x_label : str = "x") -> None :
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

    plt.tight_layout()
    plt.show()   

def error(numeric_value : list, theoric_value : list) -> float:
   return np.mean(np.abs(numeric_value - theoric_value))