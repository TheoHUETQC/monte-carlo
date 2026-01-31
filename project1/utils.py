import matplotlib.pyplot as plt

def plot2(x, y1, y2, titre1="plot 1", titre2="plot 2"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(x, y1, color='blue')
    ax1.set_title(titre1)
    ax1.set_xlabel('Axe X')
    ax1.set_ylabel('Valeurs Y1')

    ax2.plot(x, y2, color='red')
    ax2.set_title(titre2)
    ax2.set_xlabel('Axe X')
    ax2.set_ylabel('Valeurs Y2')

    plt.tight_layout()
    plt.show()