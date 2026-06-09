from src.manifolds.sphere import Sphere
import numpy as np

def simulator(T, N, dt, noise_type):
    # Initialize N particles at a point on the sphere
    points = np.tile([1.0, 0.0, 0.0], (N, 1))
    # Initialize the trajectory to an empty array to later store the new poisitions of each point in points
    trajectory = np.zeros((T, N, 3))
    
    # Initialize a sphere object
    sphere = Sphere()
        
    # Go through each time step
    for t in range(T):
        if noise_type == "isotropic":
            noise = sphere.sample_tangent_noise_multiple(points)
        elif noise_type == "anisotropic":
            noise = sphere.sample_tangent_noise_anisotropic_multiple(points)
        # Scale the noise by square root of dt
        noise_scaled = np.sqrt(dt) * noise
        # Add the noise to all of the particles in points
        points += noise_scaled
        # Project all particles back onto the sphere
        points = sphere.project_to_manifold_multiple(points)
        # Store the new positions of each point in the trajectory array
        trajectory[t] = points
    return trajectory
        
# Verify that shape of trajectory is (T, N, 3)
T = 200
N = 100
dt = 0.1
trajectory = simulator(T, N, dt, "isotropic")
assert trajectory.shape == (T, N, 3)
trajectory_two = simulator(T, N, dt, "anisotropic")
assert trajectory_two.shape == (T, N, 3)