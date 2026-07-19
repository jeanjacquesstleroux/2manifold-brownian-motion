# Import the base class that contains Manifold abstract methods
from .base import Manifold
import numpy as np

class Sphere(Manifold):
    """The Sphere class respents the unit sphere manifold. Points 
    on the manifold must therefore remain normalized and noise 
    must be tangent to the sphere.
    
    Since points on the manifold must be normalized, the magnitude 
    of a point x is equal to 1 (unit length). The tangent vector v 
    of a point x satisfies dot product of x and v is equal to 0. This 
    means they are orthogonal to each other and the tangent vector v 
    is on the tangent space of x.
    
    The Sphere class contains methods to ensure these constraints, 
    as well as a method to compute the Euler-Maruyama step for 
    the next position which is also on the manifold.
    """
    def project_to_manifold(self, x):
        '''Normalizes a point x, ensuring it is a point on the sphere.
        
        Arguments:
            x: A point in R^3 that may or may not lie on the sphere.
        
        Returns:
            The normalized form of point x.
        '''
        norm = np.linalg.norm(x)
        return x / norm
    
    def project_to_manifold_multiple(self, X):
        '''Normalizes more than one point (all the points are defined 
        as X), ensuring they are all on the sphere.
        
        Arguments:
            X: Many points in R^3 that may or may not lie on the sphere.
        
        Returns:
            The normalized form of all of the points of X.
        '''
        norms = np.linalg.norm(X, axis=1, keepdims=True)
        return X / norms
        
    def project_to_tangent(self, x, v):
        '''Removes the radial component and only returns the tangential 
        component of vector v at point x. This makes vector v lie in 
        the tangent space of point x, which represents all the possible 
        directions the point x can move while staying on the sphere.
        
        Uses the formula:
            v_tangential = v - (dot product of v and x)x
            
        This removes the component of vector v in the direction of x, 
        leaving only the component orthogonal to x.
        
        Arguments:
            x: A point on the sphere.
            v: The tangent vector in R^3 at point x, which may or may 
            not be tangent at point x.
            
        Returns:
            The component of vector v which lies in the tangent space 
            at point x.
        '''
        dot_prod = np.dot(v, x)
        return v - (dot_prod * x)
    
    def project_to_tangent_multiple(self, X, V):
        '''Removes the radial component and only returns the tangential 
        component of every vector in the group of vectors V at every point
        in the group of points X. This makes each vector in V lie in the 
        tangent space of its respective point in the group of points X, 
        which represents all the possible directions the point can move 
        while staying on the sphere.
        
        Uses the formula:
            v_tangential = v - (dot product of v and x)x
            
        This removes the component of a vector in the direction of a point, 
        leaving only the component orthogonal to the point.
        
        Arguments:
            X: A set of points on the sphere.
            V: A set of tangent vectors in R^3 which correspond to a point 
            in X, which may or may not be tangent at that point.
            
        Returns:
            The component of each vector in V which lies in the tangent space 
            of its respective point in X.
        '''
        dot_prod = np.sum(V * X, axis=1, keepdims=True)
        return V - (dot_prod * X)
        
    def sample_tangent_noise(self, x):
        '''
        Generates a random Gaussian vector in R^3 and projects it onto 
        the tangent space at point x, which is on the sphere.
        
        Arguments:
            x: A point on the sphere.
            
        Returns:
            A random Gaussian vector in R^3 which is on the tangent space 
            at point x on the sphere.
        '''
        rand_vect = np.random.randn(3)
        return self.project_to_tangent(x, rand_vect)
    
    def sample_tangent_noise_multiple(self, X):
        '''
        Generates random Gaussian vectors for many points in R^3 on the sphere 
        and projects each vector onto tangent spaceo of its respective point.
        
        Arguments:
            X: A set of points on the sphere.
            
        Returns:
            A set of random Gaussian tangent vectors in R^3.
        '''
        N = X.shape[0] # Get number of points in X
        noise = np.random.randn(N, 3)
        tangent_noise = self.project_to_tangent_multiple(X, noise)
        return tangent_noise
    
    def sample_tangent_noise_anisotropic(self, x):
        '''
        Chooses one tangent direction at point x, generates one Gaussian random 
        number and scales that tangent direction by the random number. This 
        generates Brownian noise in only one tangent direction at point x on the 
        sphere.
        
        Arguments:
            x: A point on the sphere.
            
        Returns:
            A random Gaussian tangent vector in R^3 at point x whose motion is 
            constrained to only one tangent direction.
        '''
        random_vector = np.array([1.0, 1.0, 1.0])
        tangent_vector = self.project_to_tangent(x, random_vector)
        unit_tangent_vector = tangent_vector / (np.linalg.norm(tangent_vector))
        noise = np.random.randn() # Scalar noise
        unit_tangent_vector *= noise # Vector is constrained to only one direction (such as North/South)
        return unit_tangent_vector
    
    def sample_tangent_noise_anisotropic_multiple(self, X):
        '''
        Generates anisotropic noise for many points on the sphere. Each point 
        can only move in one fixed tangent direction, which is scaled by one 
        scalar Gaussian random noise variable.
        
        Arguments:
            X: A set of points on the sphere.
            
        Returns:
            Random Gaussian tangent vectors in R^3.
        '''
        N = X.shape[0] # Get number of points in X
        vector = np.array([1.0, 1.0, 1.0]) # Chosen tangent vector for each point in X
        # Keep only the tangential component of every tangent vector respect to a point in X
        tangent_directions = self.project_to_tangent_multiple(X, np.tile(vector, (N, 1)))
        unit_tangent_directions = tangent_directions / (np.linalg.norm(tangent_directions, axis=1, keepdims=True))
        noise = np.random.randn(N, 1)
        anisotropic_noise = unit_tangent_directions * noise # Noise in only one direction (along the vector)
        return anisotropic_noise
        
    def euler_maruyama_step(self, x, dt):
        '''Simulates one step of Brownian motion from point x to the next 
        point on the sphere. Noise is first generated for point x and 
        then scaled by the square root of the time step. Then the next 
        point becomes the previous plus the scaled noise and must be 
        projected onto the sphere.
        
        Variance measures how spread out the random positions are. It grows 
        linearly with time (t). Standard deviation is the square root of 
        variance and represents the net displacement (the distance from the 
        start). Hence, the distance the walker travels from the starting point 
        increases with the square root of t.
        
        The formula used to find the noise scaled is:
            Change in W_t = square root of change in t * Z, Z ~ N(0, 1)
            
        where change in W_t is the total random change in the system for the respective 
        time step, t is the time step and Z is the standard normal random 
        noise.
        
        Arguments:
            x: A point on the sphere.
            dt: A time step.
            
        Returns:
            The next point on the sphere.
        '''
        noise = self.sample_tangent_noise(x)
        noise_scaled = np.sqrt(dt) * noise
        x += noise_scaled
        return self.project_to_manifold(x)
        