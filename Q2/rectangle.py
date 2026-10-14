class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

rectangle = Rectangle(3, 4)
rectangle.width = 5
rectangle.height = 6
print(rectangle.width)
print(rectangle.height)
@property
def height(self) :
return f"(self._height: .1f}cm"
@width.setter
def width(self, new width) :
if new width > 0:
self._width = new width
@height. setter
def height(self, new_height) :
if new height › 0:
self._height = new height
else:
print("Height must be greater than zero")
rectangle = Rectangle (3, 4)
rectangle.width = 5
rectangle.height = 6
print (rectangle.width)
print (rectangle.height)