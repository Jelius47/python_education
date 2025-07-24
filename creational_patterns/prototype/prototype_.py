'''The good news is python provides fuctionality for this you just import 
the library 
== Useful when want to test some stuffs that you havee a copy a portion of an existing object
   without caring to reecreate it again  '''

import copy
from abc import ABC,abstractmethod



class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Square(Shape):
    def __init__(self,size):
        self.size = size
    def draw(self):
        print(f"Drawing a squre of size {self.size}")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def draw(self):
        print(f"Drawing the Circle of radius: {self.radius}")



class AbstractArt:
    def __init__(self, bg_colors,shapes):
        self.bg_colors = bg_colors
        self.shapes = shapes
    
    def draw(self):
        print(f"Background color is {self.bg_colors}") 
        [x.draw() for x in shapes]
        
       
if __name__ == "__main__`":
    shapes = [Square(5),Square(3), Circle(3)]

    art1 = AbstractArt(bg_colors="red",shapes=shapes)


    # Now using the copty functionality
    # copy() - will copy the object by reference of the actual class
    # deepcopy() - will copy the object itself as whole 

    art2 = copy.copy(art1)


    # Testing the facts if they works  
    art1.draw()
    art2.draw()