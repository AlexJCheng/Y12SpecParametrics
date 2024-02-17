import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


# Define the parameter range
range = int(round(4*np.pi, 0))
t = np.linspace(0, range, range* 10)
sq = True
gsize = 2
a = 1
b = 1
c = 0
d = 0
e = 1 
f = 1
g = 0
h = 0 
m = 1
n = 1

# Define the parametric equations
x = a * np.cos(b * t + c)**m + d
y = e * np.sin(f * t + g)**n + h
y = y * 1j # Multiply y by i

# Create the plot
fig, ax = plt.subplots(figsize=(6,6))
line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'ro')  # This is the point that will follow the plot

# Set labels and title
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title(f'x = cos({b}t), y = sin({f}t)')

# Add thick lines at x=0 and y=0
plt.axhline(0, color='black', linewidth=1)  # Horizontal line (y=0)
plt.axvline(0, color='black', linewidth=1)  # Vertical line (x=0)

# Set the limits of x and y axes
if sq == True:
    ax.set_xlim(-gsize, gsize)
    ax.set_ylim(-gsize, gsize)

# Equal aspect ratio ensures that the scale on the x-axis is the same as the y-axis
ax.set_aspect('equal', adjustable='box')

# Show grid
ax.grid(True)

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Animation function which updates figure data
def animate(i):
    line.set_data(x.real[:i], y.imag[:i])
    point.set_data(x.real[i], y.imag[i])  # Update the point's position here
    return line, point,

# Call the animator
ani = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=20, blit=True)


# Save the animation as a mp4 video file
ani.save(f'x = cos(tt), y = sin(t).gif', writer="ffmpeg")

# Show the plot
plt.show()
