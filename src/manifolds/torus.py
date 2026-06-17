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
    