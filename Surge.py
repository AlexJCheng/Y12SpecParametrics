import matplotlib.pyplot as plt
import numpy as np

# Define the domain
global x
x = np.linspace(-10, 20, 500)

# Plot size
ymin = 0
ymax = 5
ystep = 0.5
xmin = 0
xmax = 10
xstep = 1

def calc_eq(a, k):
    y = a * x * np.e ** (-1 * k * x)
    return y

def plot_setup():
    plt.figure(figsize=(6,6))
    
    # Add thick lines at x=0 and y=0
    plt.axhline(0, color='black', linewidth=1)  # Horizontal line (y=0)
    plt.axvline(0, color='black', linewidth=1)  # Vertical line (x=0)

    # Set labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Surge Function')

    # Set the limits of x and y axes
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    # Show grid
    plt.grid(which = 'major', linewidth = 0.5)
    plt.xticks(np.arange(xmin,xmax+xstep,xstep))
    plt.yticks(np.arange(ymin,ymax+ystep,ystep))

def plot_max(k, y):
    plt.plot(1/k, max(y), marker = 'o')
    plt.annotate(f'({1/k}, {round(max(y),2)})', (1/k + 0.3, max(y)))

def main():
    plot_setup()
    a = [0.5, 1, 5, 10]
    k = 1

    for i in a:
        y = calc_eq(i, k)
        plt.plot(x, y, label = f'{i}xe^(-{k}x)')
        plot_max(k, y) 
    plt.legend()
    plt.savefig(f'S{a}xe^(-{k}x).png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()

