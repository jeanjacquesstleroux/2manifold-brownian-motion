# Import the base class that contains Manifold abstract methods
from .base import Manifold
import numpy as np
import math

class Torus(Manifold):
    """Add summary here
    """
    def __init__(self, R, r):
        """Initializes the major and minor radii that define the torus' 
        geometry.
        
        Arguments: 
            R: Distance from the center of the central hole to the center 
            of the tube.
            r: Radius of the tube.
        """
        self.R = R
        self.r = r
        
    def parametrize(self, u, v):
        """Converts parameters (u, v) on the torus to Cartesian (x, y, z) 
        coordinates. Uses formulas
        
        x(u, v) = (R + rcos(v))cos(u)
        y(u, v) = (R + rcos(v))sin(u)
        z(u, v) = rsin(v)
        
        The toroidal angle (u) ranges from 0 to 2 pi and rotates around the 
        main z-axis. The poloidal angle (v) ranges from 0 to 2 pi and rotates 
        around the circular cross section of the tube.

        Arguments:
            u: The toroidal angle of the torus.
            v: The poloidal angle of the torus.

        Returns:
            The Cartesian coordinates of a point on the torus.
        """
        x = (self.R + self.r * math.cos(v)) * math.cos(u)
        y = (self.R + self.r * math.cos(v)) * math.sin(u)
        z = self.r * math.sin(v)
        point = np.array([x, y, z])
        return point
    
    def normal_vector(self, u, v):
        """Computes the unit normal vector at a point on the torus. 
        The normal vector points perpendicular to the torus (away from the 
        tube at that location).
        
        Uses the analytic formula for the torus normal, expressed as 
        
        N(u, v) = (cos(u)cos(v), sin(u)cos(v), sin(v))
        
        The Cartesian components of the normal vector are
        
        x = cos(u)cos(v),
        y = sin(u)cos(v),
        z = sin(v)

        Arguments:
            u: The toroidal angle of the torus.
            v: The poloidal angle of the torus.

        Returns:
            The Cartesian coordinates of the unit normal vector at a 
            point on the torus.
        """
        x = math.cos(u) * math.cos(v)
        y = math.sin(u) * math.cos(v)
        z = math.sin(v)
        normal_vector = np.array([x, y, z])
        return normal_vector
    
    def project_to_tangent(self, u, v, vector):
        """Projects a vector onto the tangent plane of the torus. This 
        is done by removing the normal component of the vector and only 
        leaving the tangential component.
        
        The dot product of the vector and the unit normal vector measures 
        how much of the vector points in the normal direction (away from 
        the torus). When multiplied by the unit normal vector, it is the 
        normal component of the vector.
        
        The formula used to find the tangential component of the vector is 
        
        tangential_vector = vector - (dot product of vector and N) * N
        
        where N is the normal vector.

        Arguments:
            u: The toroidal angle of the torus.
            v: The poloidal angle of the torus.
            vector: An arbitrary vector.

        Returns:
            The tangential vector at (u, v).
        """
        normal = self.normal_vector(u, v)
        tangential_vector = vector - (np.dot(vector, normal)) * normal
        return tangential_vector
    
    def sample_tangent_noise(self, x):
        '''
        Generates a random Gaussian vector in R^3 and projects it onto 
        the tangent space at point x, which is on the torus.
        
        The Cartesian point x is first converted into its corresponding 
        parameters (u, v) using the torus' geometry. Then a random Euclidean 
        vector is generated and projected onto tangent space of point x.
        
        Arguments:
            x: A point on the torus.
            
        Returns:
            A random Gaussian vector in R^3 which is on the tangent space 
            at point x on the sphere.
        '''
        rand_vect = np.random.randn(3)
        x_coor = x[0]
        y_coor = x[1]
        z_coor = x[2]
        u = math.atan2(y_coor, x_coor)
        rho = math.sqrt(x_coor**2 + y_coor**2)
        v = math.atan2(z_coor, rho - self.R)
        return self.project_to_tangent(u, v, rand_vect)
    
    def project_to_manifold(self, x):
        '''Projects a point in R^3 onto the torus. The projection is computed 
        analytically rather than numerically. 
        
        A torus consists of a large circle (radius R) and small circles (radius 
        r) on every cross-section of the large circle.
        
        First, the nearest point on the major circle of radius R in the xy-plane 
        is computed. This point is used as the center of the nearest tube 
        cross-section of the torus. The offset is then computed from the tube center 
        to the input point. It is normalized and scaled to the length of the tube's 
        radius, which is r. The endpoint of the scaled offset vector is the nearest 
        point on the torus, which is returned.
        
        Arguments: 
            x: A point in R^3 that may or may not be on the torus.
        
        Returns:
            The nearest point on the torus from the input point.
        '''
        x_coor = x[0]
        y_coor = x[1]
        
        distance_from_z = math.sqrt(x_coor**2 + y_coor**2)
        center_x = self.R * (x_coor / distance_from_z)
        center_y = self.R * (y_coor / distance_from_z)
        center = np.array([center_x, center_y, 0])
        
        offset = x - center
        offset_norm = np.linalg.norm(offset)
        unit_offset = offset / offset_norm
        
        point = center + self.r * unit_offset
        return point