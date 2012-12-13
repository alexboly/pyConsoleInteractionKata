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

    def askForShape(self):
        self.console.printMessage(self.message)
        shapeType = self.console.readString()
        
        if shapeType == self.rectangleShapeType:
            self.console.printMessage(self.rectangleWidthMessage)
            width = self.console.readFloat()
            self.console.printMessage(self.rectangleHeightMessage)
            height = self.console.readFloat()
            self.console.printMessage("Area is {0:.2f}".format(width * height))
            self.console.printMessage("Circumference is {0}".format(2 * (width + height)))

        if shapeType == self.circleShapeType:
            radius = self.console.readFloat(self.circleRadiusMessage)
            self.console.printMessage("Area is {0:.2f}".format(3.14 * radius * radius))
            self.console.printMessage("Circumference is {0:.2f}".format(2 * 3.14 * radius))

class Console:
   
    def readString(self):
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
        when(self.consoleMock).readString().thenReturn(self.shapeInput.circleShapeType)
        when(self.consoleMock).readFloat(self.shapeInput.circleRadiusMessage).thenReturn(radius)

    def consoleMockForRectangle(self, width, height):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.rectangleShapeType)
        when(self.consoleMock).readFloat().thenReturn(width).thenReturn(height)

    def testPrintsMessageWhenAskingForShape(self):
        self.shapeInput.askForShape()

        verify(self.consoleMock).printMessage(self.shapeInput.message)

    def testAsksForWidthIfRectangle(self):
        self.consoleMockForRectangle(100, 10)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.rectangleWidthMessage)
        
    def testAsksForHeightIfRectangle(self):
        self.consoleMockForRectangle(100, 10)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.rectangleHeightMessage)
        
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
        
        verify(self.consoleMock).printMessage("Circumference is 400")

    def testPrintsCircleCircumference(self):
        self.consoleMockForCircle(100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Circumference is 628.00")

if __name__ == "__main__":
    main()