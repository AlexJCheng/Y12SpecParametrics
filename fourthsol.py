import matplotlib.pyplot as plt
import numpy as np

# Define the parameter range
t = np.linspace(0, 20, 2000)
gsize = 20
a = -10

# Define the parametric equations
x = a * t ** 2
#

y = a * t ** (-1)
#

y = y * 1j # Multiply y by i



# Create the plot
plt.figure(figsize=(6,6))
plt.plot(x.real, y.imag)  # x is real, y is imaginary

# Add thick lines at x=0 and y=0
plt.axhline(0, color='black', linewidth=1)  # Horizontal line (y=0)
plt.axvline(0, color='black', linewidth=1)  # Vertical line (x=0)

# Set labels and title
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Parametric Curve on Argand Diagram')

# Set the limits of x and y axes

plt.xlim(-gsize, gsize)
plt.ylim(-gsize, gsize)

# Equal aspect ratio ensures that the scale on the x-axis is the same as the y-axis
plt.gca().set_aspect('equal', adjustable='box')

# Show grid
plt.grid(True)

# Show the plot
plt.show()
