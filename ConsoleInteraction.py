# See https://sites.google.com/site/tddproblems/all-problems-1/Console-interaction for problem description
from mockito import *
from unittest.case import TestCase
import os
from google.protobuf.text_format import PrintMessage


class ShapeInput():

    message = "Shape: (C)ircle or (R)ectangle?"
    circleRadiusMessage = "Circle radius is: "
    rectangleWidthMessage = "Rectangle width is: "
    rectangleShapeType = 'R'
    circleShapeType = 'C'
    rectangleHeightMessage = "Rectangle height is:"
    
    def __init__(self, console):
        self.console = console


    def readCircleRadius(self):
        return self.console.readFloat(self.circleRadiusMessage)


    def computeCircleArea(self, radius):
        return 3.14 * radius * radius

    def computeCircleCircumference(self, radius):
        return 2 * 3.14 * radius


    def readRectangleWidth(self):
        return self.console.readFloat(self.rectangleWidthMessage)


    def readRectangleHeight(self):
        return self.console.readFloat(self.rectangleHeightMessage)


    def computeRectangleArea(self, width, height):
        return width * height


    def computeRectangleCircumference(self, width, height):
        return 2 * (width + height)

    def askForShape(self):
        shapeType = self.console.readString(self.message)

        if shapeType == self.rectangleShapeType:
            width = self.readRectangleWidth()
            height = self.readRectangleHeight()
            area = self.computeRectangleArea(width, height)
            circumference = self.computeRectangleCircumference(width, height)

        if shapeType == self.circleShapeType:
            radius = self.readCircleRadius()
            area = self.computeCircleArea(radius)
            circumference = self.computeCircleCircumference(radius)

        self.console.printMessage("Area is {0:.2f}".format(area))
        self.console.printMessage("Circumference is {0:.2f}".format(circumference))

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
    shapeInput.askForShape()

class ConsoleInteractionTests(TestCase):

    def setUp(self):
        self.consoleMock = mock()
        self.shapeInput = ShapeInput(self.consoleMock)
        
    def consoleMockForCircle(self, radius):
        when(self.consoleMock).readString(self.shapeInput.message).thenReturn(self.shapeInput.circleShapeType)
        when(self.consoleMock).readFloat(self.shapeInput.circleRadiusMessage).thenReturn(radius)

    def consoleMockForRectangle(self, width, height):
        when(self.consoleMock).readString(self.shapeInput.message).thenReturn(self.shapeInput.rectangleShapeType)
        when(self.consoleMock).readFloat(self.shapeInput.rectangleWidthMessage).thenReturn(width)
        when(self.consoleMock).readFloat(self.shapeInput.rectangleHeightMessage).thenReturn(height)

    def testPrintsCorrectRectangleArea(self):
        self.consoleMockForRectangle(100, 100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Area is 10000.00")
        
    def testPrintsSecondCorrectRectangleArea(self):
        self.consoleMockForRectangle(10, 100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Area is 1000.00")
        
    def testPrintsCorrectCircleArea(self):
        self.consoleMockForCircle(100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Area is 31400.00")

    def testPrintsSecondCorrectCircleArea(self):
        self.consoleMockForCircle(200)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Area is 125600.00")

    def testPrintsRectangleCircumference(self):
        self.consoleMockForRectangle(100, 100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Circumference is 400.00")

    def testPrintsCircleCircumference(self):
        self.consoleMockForCircle(100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Circumference is 628.00")

if __name__ == "__main__":
    main()