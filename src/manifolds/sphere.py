# Import the base class that contains Manifold abstract methods
from base import Manifold
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
        