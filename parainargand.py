import matplotlib.pyplot as plt
import numpy as np

# Define the parameter range
t = np.linspace(0, 30, 300)
sq = False
gsize = 5
a = 1
b = 1
c = 0
d = 0
e = 1
f = 1
g = 0
h = t
m = 1
n = 1

# Define the parametric equations
x = a * np.cos(b * t + c)**m + d
# x = a cos(bt + c) + d

y = e * np.sin(f * t + g)**n + h
# y = e sin(ft + g) + h

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
#plt.title("Parametric Curve on Argand Diagram")
#plt.title(f'x = {a}cos({b}t+{c})+({d}), y = {e}cos({f}t+{g})+({h})')
plt.title(f'x = {a}cos(t)+(0), y = {e}sin(t)+(t)')

# Plot the start and end points
plt.scatter(x.real[0], y.imag[0], color='green')  # Start point in green
plt.scatter(x.real[10], y.imag[10], color='blue')  # Indicator point in blue
plt.scatter(x.real[-1], y.imag[-1], color='red')  # End point in red

# Set the limits of x and y axes
if sq == True:
    plt.xlim(-gsize, gsize)
    plt.ylim(-gsize, gsize)

# Equal aspect ratio ensures that the scale on the x-axis is the same as the y-axis
plt.gca().set_aspect('equal', adjustable='box')

# Show grid
plt.grid(True)

# Show the plot
plt.show()
print(x[-1], y[-1])
