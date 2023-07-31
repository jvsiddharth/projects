import numpy as np
import matplotlib.pyplot as plt

def chaos_game(num_vertices, num_iterations):
    # Step 1: Set up the environment
    vertices = generate_polygon_vertices(num_vertices)
    point = np.random.rand(2)  # Random starting point within [0, 1)

    # Step 2-4: Iteratively generate points
    points = np.zeros((num_iterations, 2))
    for i in range(num_iterations):
        vertex = vertices[np.random.randint(num_vertices)]  # Random vertex
        point = (point + vertex) / 2  # Midpoint calculation
        points[i] = point

    return points

def generate_polygon_vertices(num_vertices):
    angles = 2 * np.pi * np.arange(num_vertices) / num_vertices
    x = np.cos(angles)
    y = np.sin(angles)
    return np.column_stack((x, y))

# User-specified parameters
num_vertices = int(input("Enter the number of vertices for the polygon: "))
num_iterations = int(input("Enter the number of iterations for the fractal Game: "))

# Generate points using the Chaos Game
points = chaos_game(num_vertices, num_iterations)

# Visualize the fractal
plt.scatter(points[:, 0], points[:, 1], s=1, c='black')
plt.axis('off')
plt.show()