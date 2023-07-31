import numpy as np
import matplotlib.pyplot as plt

def lorenz_attractor(x, y, z, sigma=10, rho=28, beta=8/3, dt=0.01, num_steps=10000):
    points = np.zeros((num_steps, 3))
    for i in range(num_steps):
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dx * dt
        y += dy * dt
        z += dz * dt
        points[i] = [x, y, z]
    return points

# Parameters
sigma = 10
rho = 28
beta = 8/3
dt = 0.01
num_steps = 10000

# Initial conditions
x0 = 1.0
y0 = 0.0
z0 = 0.0

# Generate Lorenz attractor points
points = lorenz_attractor(x0, y0, z0, sigma, rho, beta, dt, num_steps)

# Plot the attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(points[:, 0], points[:, 1], points[:, 2], lw=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz Attractor')
plt.show()
