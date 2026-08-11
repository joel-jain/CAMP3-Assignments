from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
        def __init__(self,radius):
            self.radius=radius

        def area(self):
             return 3.14 *self.radius**2

class Recatengle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
c=Circle(5)
r=Recatengle(10,4)
print("Circle Area:",c.area())
print("Rectangle Area:",r.area())