import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initial positions of the isotopes
initial_position_d = (-2, 0, 0)  # Deuterium
initial_position_t = (2, 0, 0)   # Tritium

# Final positions of the products
final_position_helium = (1, 1, 1)  # Helium
final_position_neutron = (-1, 1, 1)  # Neutron

# Set up the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 2)
ax.set_zlim(0, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Time')

# Draw initial positions of isotopes
ax.scatter(*initial_position_d, label='Deuterium (D)', color='blue', marker='o')
ax.scatter(*initial_position_t, label='Tritium (T)', color='red', marker='o')

# Draw final positions of products
ax.scatter(*final_position_helium, label='Helium (He)', color='green', marker='o')
ax.scatter(*final_position_neutron, label='Neutron (n)', color='purple', marker='o')

# Draw the path of the isotopes during the reaction
ax.plot([initial_position_d[0], final_position_helium[0]], [initial_position_d[1], final_position_helium[1]],
        [initial_position_d[2], final_position_helium[2]], color='green', linestyle='--')
ax.plot([initial_position_t[0], final_position_neutron[0]], [initial_position_t[1], final_position_neutron[1]],
        [initial_position_t[2], final_position_neutron[2]], color='purple', linestyle='--')

# Add annotations
ax.text(0, 0, 1.5, 'Fusion Reaction', color='black')
ax.text(final_position_helium[0] + 0.5, final_position_helium[1] + 0.2, final_position_helium[2] + 0.2, 'Helium (He)',
        color='black')
ax.text(final_position_neutron[0] + 0.5, final_position_neutron[1] + 0.2, final_position_neutron[2] + 0.2, 'Neutron (n)',
        color='black')

# Add legend
ax.legend()

# Show the 3D plot
plt.show()
