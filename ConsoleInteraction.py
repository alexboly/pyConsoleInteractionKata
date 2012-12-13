# See https://sites.google.com/site/tddproblems/all-problems-1/Console-interaction for problem description
from mockito import *
from unittest.case import TestCase

class Rectangle:

    rectangleShapeType = 'R'
    rectangleWidthMessage = "Rectangle width is: "
    rectangleHeightMessage = "Rectangle height is:"
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def circumference(self):
        return 2 * (self.width + self.height)
    
    @classmethod
    def read(self, console):
        width = console.readFloat(self.rectangleWidthMessage)
        height = console.readFloat(self.rectangleHeightMessage)
        return Rectangle(width, height)

class Circle:

    circleShapeType = 'C'
    circleRadiusMessage = "Circle radius is: "
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius

    @classmethod
    def read(self, console):
        radius = console.readFloat(self.circleRadiusMessage)
        return Circle(radius)

class ShapeInput():

    message = "Shape: (C)ircle or (R)ectangle?"
    
    def __init__(self, console):
        self.console = console

    def readShapeDetails(self, shapeType):
        isRectangle = shapeType == Rectangle.rectangleShapeType
        return Rectangle.read(self.console) if isRectangle else Circle.read(self.console)

    def readShapeType(self):
        return self.console.readString(self.message)

    def printArea(self, shape):
        return self.console.printMessage("Area is {0:.2f}".format(shape.area()))

    def printCircumference(self, shape):
        return self.console.printMessage("Circumference is {0:.2f}".format(shape.circumference()))

    def printShapeAreaAndCircumference(self):
        shapeType = self.readShapeType()
        shape = self.readShapeDetails(shapeType)
        self.printArea(shape)
        self.printCircumference(shape)

class Console:
   
    def readString(self, message = ""):
        self.printMessage(message)
        return raw_input()
    
    def readFloat(self, message = ""):
        self.printMessage(message)
        return float(raw_input())
    
    def printMessage(self, message):
        print message

def main():
    console = Console()
    shapeInput = ShapeInput(console)
    shapeInput.printShapeAreaAndCircumference()

class ConsoleInteractionTests(TestCase):

    def setUp(self):
        self.consoleMock = mock()
        self.shapeInput = ShapeInput(self.consoleMock)
        
    def consoleMockForCircle(self, radius):
        when(self.consoleMock).readString(self.shapeInput.message).thenReturn(Circle.circleShapeType)
        when(self.consoleMock).readFloat(Circle.circleRadiusMessage).thenReturn(radius)

    def consoleMockForRectangle(self, width, height):
        when(self.consoleMock).readString(self.shapeInput.message).thenReturn(Rectangle.rectangleShapeType)
        when(self.consoleMock).readFloat(Rectangle.rectangleWidthMessage).thenReturn(width)
        when(self.consoleMock).readFloat(Rectangle.rectangleHeightMessage).thenReturn(height)

    def testPrintsCorrectRectangleArea(self):
        self.consoleMockForRectangle(100, 100)
        
        self.shapeInput.printShapeAreaAndCircumference()
        
        verify(self.consoleMock).printMessage("Area is 10000.00")
        
    def testPrintsSecondCorrectRectangleArea(self):
        self.consoleMockForRectangle(10, 100)
        
        self.shapeInput.printShapeAreaAndCircumference()
        
        verify(self.consoleMock).printMessage("Area is 1000.00")
        
    def testPrintsCorrectCircleArea(self):
        self.consoleMockForCircle(100)
        
        self.shapeInput.printShapeAreaAndCircumference()
        
        verify(self.consoleMock).printMessage("Area is 31400.00")

    def testPrintsSecondCorrectCircleArea(self):
        self.consoleMockForCircle(200)
        
        self.shapeInput.printShapeAreaAndCircumference()
        
        verify(self.consoleMock).printMessage("Area is 125600.00")

    def testPrintsRectangleCircumference(self):
        self.consoleMockForRectangle(100, 100)
        
        self.shapeInput.printShapeAreaAndCircumference()
        
        verify(self.consoleMock).printMessage("Circumference is 400.00")

    def testPrintsCircleCircumference(self):
        self.consoleMockForCircle(100)
        
        self.shapeInput.printShapeAreaAndCircumference()
        
        verify(self.consoleMock).printMessage("Circumference is 628.00")

if __name__ == "__main__":
    main()