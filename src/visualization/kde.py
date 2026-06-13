import numpy as np
import math

# Plot the empirical surface distribution (KDE heatmap on the sphere)

def sphere_kde(final_positions, x_surface, y_surface, z_surface, k=None, N=None):
    # Flatten each 2D surface to a coordinate on the sphere surface
    x_one_dim = x_surface.flatten()
    y_one_dim = y_surface.flatten()
    z_one_dim = z_surface.flatten()

    # Put the coordinates as points on the mesh surface
    mesh = np.stack([x_one_dim, y_one_dim, z_one_dim], axis=1)

    # Choose the value of k parameter
    if k is None:
        k = 20
    else:
        k = math.sqrt(N)

    # Compute all the dot products
    mesh = mesh.transpose()  # shape becomes (3, M)
    dot_prod = np.dot(final_positions, mesh)

    # Apply k to get the weights
    weights = np.exp(k * dot_prod)

    # Add up all the weights for each mesh point
    density = np.sum(weights, axis=0)

    # Normalize the density by dividing by the maximum
    density /= density.max()

    # Reshape density back onto the sphere grid
    density = density.reshape(x_surface.shape)
    
    return density