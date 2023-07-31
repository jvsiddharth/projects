import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Constants
hbar = 1.0  # Reduced Planck's constant
m = 1.0  # Mass of the particle
L = 1.0  # Length of the well in each dimension
num_points = 10  # Number of grid points
dx = L / (num_points - 1)  # Grid spacing
dt = 0.01  # Time step
num_steps = 100  # Number of time steps

# Spatial grid
x = np.linspace(0, L, num_points)
y = np.linspace(0, L, num_points)
z = np.linspace(0, L, num_points)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Wave function
psi = np.zeros((num_points, num_points, num_points), dtype=complex)
psi[1:num_points - 1, 1:num_points - 1, 1:num_points - 1] = (
    np.random.rand(num_points - 2, num_points - 2, num_points - 2) +
    1j * np.random.rand(num_points - 2, num_points - 2, num_points - 2))
psi /= np.linalg.norm(psi)

# Hamiltonian matrix
H = np.zeros((num_points, num_points, num_points), dtype=complex)
H += np.diag(-2.0 / dx**2 - np.zeros(num_points), k=0)  # Diagonal elements
H += np.diag(1.0 / dx**2 * np.ones(num_points - 1), k=1)  # Upper diagonal
H += np.diag(1.0 / dx**2 * np.ones(num_points - 1), k=-1)  # Lower diagonal

# Set up the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Time evolution')

# Initialize an empty scatter plot
scatter = ax.scatter([], [], [], c=[], cmap='viridis')

# Function to update the scatter plot at each time step
def update(step):
    global psi, scatter
    # Compute the next time step using the finite difference method
    psi += -1j * dt / (2 * m * hbar) * (
        (H @ psi + psi @ H + psi @ H @ psi) - 2 * np.sum(psi * (H @ psi)) / np.sum(psi**2) * psi)

    # Normalize the wave function at each step
    psi /= np.linalg.norm(psi)

    # Compute the probability density
    prob_density = np.abs(psi)**2

    # Update the scatter plot data
    scatter._offsets3d = (X.flatten(), Y.flatten(), Z.flatten())
    scatter.set_array(prob_density.flatten())

# Create the animation
animation = FuncAnimation(fig, update, frames=num_steps, interval=200)

# Display the animation
plt.show()

# Compute eigenstates and eigenvalues
eigenvalues, eigenvectors = np.linalg.eigh(H)

# Sort eigenvalues and eigenvectors in ascending order
sort_indices = np.argsort(eigenvalues)
eigenvalues = eigenvalues[sort_indices]
eigenvectors = eigenvectors[:, sort_indices]

# Plot the eigenstates
fig_eigenstates = plt.figure()
ax_eigenstates = fig_eigenstates.add_subplot(111, projection='3d')
ax_eigenstates.set_xlabel('X')
ax_eigenstates.set_ylabel('Y')
ax_eigenstates.set_zlabel('Z')
ax_eigenstates.set_title('Eigenstates of the Hamiltonian')

for i in range(num_points):
    # Get the i-th eigenstate
    eigenstate = eigenvectors[:, i]

    # Compute the probability density
    prob_density = np.abs(eigenstate)**2

    # Plot the eigenstate
    ax_eigenstates.scatter(X.flatten(), Y.flatten(), Z.flatten(), c=prob_density.flatten(), cmap='viridis', alpha=0.5)

# Show the plot
plt.show()
