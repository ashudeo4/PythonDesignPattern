from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color =  color
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def description(self):
        print(f"{self.__class__.__name__} has the color: {self.color}")

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    def description(self):
        return super().description()
    
def process_my_color(obj: Shape):
    obj.description()
    
rectangle = Rectangle(4, 5, "red")
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter {rectangle.perimeter()}")

process_my_color(rectangle)