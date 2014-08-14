"""

This is the render system for a given lsystem this class is designed to be the entry point for displaying
and visualising lsystems and will eventualy have both 2d and 3d rendering capabilities.

The 2D rendering is provided by the turtle graphics api, the 3d will be far more complex and involve the 
opengl bindings for python

This is the base render defines a render system and a basic api to handle displaying a single lsystem product

This class should function like a java interface until i find out how to do interfaces in the pythonic way

TODO refine this documention also find out right place to put
"""

import abc

class rendersystem(object):
    __metaclass__ = abc.ABCMeta
    
    
    @abc.abstractmethod
    def draw(self,word):
        """ 
        
        Should render a word that has been produced by the lsystem the onus is on the subclass to decide how and
        what to draw and if the word is valid

        """
        raise NotImplementedError
        
