from src.manifolds.sphere import Sphere
from src.manifolds.torus import Torus
import numpy as np

# Simulator function for predefined points - for Notebook 2
def simulator(T, N, dt, noise_type, starting_point=None):
    # Initialize a sphere object
    sphere = Sphere()
    
    # Initialize N particles at a point on the sphere
    if starting_point is None:
        points = np.tile([1.0, 0.0, 0.0], (N, 1))
    else:
        starting_point = sphere.project_to_manifold(starting_point) # Avoid floating point errors, ensure point is on sphere
        points = np.tile(starting_point, (N, 1))
    # Initialize the trajectory to an empty array to later store the new poisitions of each point in points
    trajectory = np.zeros((T, N, 3))
        
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

# Vectorized simulator for the torus (isotropic noise only - anisotropic
# noise is not yet implemented for the Torus manifold)
def torus_simulator(T, N, dt, R, r, starting_point=None):
    torus = Torus(R, r)

    if starting_point is None:
        starting_point = torus.parametrize(0.0, 0.0)
    points = np.tile(starting_point, (N, 1))
    trajectory = np.zeros((T, N, 3))

    for t in range(T):
        noise = torus.sample_tangent_noise_multiple(points)
        noise_scaled = np.sqrt(dt) * noise
        points = points + noise_scaled
        points = torus.project_to_manifold_multiple(points)
        trajectory[t] = points
    return trajectory


if __name__ == "__main__":
    # Verify that shape of trajectory is (T, N, 3)
    T = 200
    N = 100
    dt = 0.01
    trajectory = simulator(T, N, dt, "isotropic")
    assert trajectory.shape == (T, N, 3)
    trajectory_two = simulator(T, N, dt, "anisotropic")
    assert trajectory_two.shape == (T, N, 3)
    trajectory_three = torus_simulator(T, N, dt, R=3, r=1)
    assert trajectory_three.shape == (T, N, 3)