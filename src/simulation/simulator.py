from src.manifolds.sphere import Sphere
import numpy as np

def simulator(T, N, dt):
    # Initialize N particles at a point on the sphere
    points = np.tile([1.0, 0.0, 0.0], (N, 1))
    # Initialize the trajectory to an empty array to later store the new poisitions of each point in points
    trajectory = np.zeros((T, N, 3))
    
    # Initialize a sphere object
    sphere = Sphere()
    # Set up random number generator
    rng = np.random.default_rng()
    
    # Go through each time step
    for t in range(T):
        # Create random noise of shape (N, 3) for each point in points using random number generator
        noise = rng.standard_normal((N, 3))
        # Project each noise vector onto the tangent space of its particle
        noise = sphere.project_to_tangent_multiple(points, noise)
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
trajectory = simulator(T, N, dt)
assert trajectory.shape == (T, N, 3)