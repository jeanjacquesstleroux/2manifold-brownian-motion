from abc import ABC, abstractmethod

class Manifold(ABC):
    """
    Abstract base class for manifold implementations.
    
    A manifold is a space that has constraints.
    
    Every subclass of Manifold should implement methods 
    to project vectors onto tangent spaces, project points 
    back onto the manifold and sample tangent-space noise.
    """
    
    @abstractmethod
    def project_to_tangent(self, x, v):
        """
        Projects a vector v onto the tangent space at point x.
        
        The tangent space is directions that a point x is able to
        move to while it stays on the manifold. It is also known 
        as the local approximation at a point.
        
        The vector v may be pointing to the manifold, violating the
        geometry of the mainfold, or pointing off the manifold. This
        method ensures that the returned vector satisfies manifold 
        constraints.
        
        Arguments:
            x: A point on the manifold.
            v: The vector to project.
            
        Returns:
            A tangent vector at x.
        """
        pass
    
    @abstractmethod
    def project_to_manifold(self, x):
        """
        Projects a point x onto the manifold.
        
        The point x may be slighly off of the manifold due to numerical 
        computations throughout the algorithm. This method ensures the
        point x is projected back onto the manifold before it is used 
        again.
        
        Arguments:
            x: A point that may not be on the manifold.
            
        Returns:
            A point on the manifold.
        """
        pass
    
    @abstractmethod
    def sample_tangent_noise(self, x):
        """
        Generates a vector which lies in the tangent space at point x.
        It represents sample noise because the returned vector is random.
        
        Random Euclidean noise does not always keep the point x on 
        the manifold. This method ensures that the genereated noise lies 
        entirely within the tangent space at point x on the manifold.
        
        Arguments:
            x: A point on the manifold.
            
        Returns:
            A noise vector in tangent space.
        """
        pass