from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    def __init__(self, c):
        self.color = c

    def get_color(self):
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        pass


# Square Class extends Shape
class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self) -> float:
        return self.side * self.side


# -------- Driver Code --------
if __name__ == "__main__":
    sq = Square("Blue", 5)
    print("Color of square:", sq.get_color())
    print("Area of square:", sq.get_area())
