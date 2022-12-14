#!/usr/bin/python3

"""
Real definition of a rectangle
"""

class Rectangle:
    """ 
    
    Represent a real definition of a rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle.
        Args:
        width (int) : the width of the new rectangle
        height (int) : the height of the new rectangle
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """ Get/set the current width of a rectangle """
        return (self.__width)
    
    def height(self):
        """ Get/set the current height of a rectangle """
        return (self.__height)
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0: 
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @height.setter
    def height(self, value)
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    elif value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value
