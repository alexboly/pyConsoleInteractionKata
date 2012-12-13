# See https://sites.google.com/site/tddproblems/all-problems-1/Console-interaction for problem description
from mockito import *
from unittest.case import TestCase
import math


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

        if shapeType == self.circleShapeType:
            self.console.printMessage(self.circleRadiusMessage)
            radius = self.console.readFloat()
            self.console.printMessage("Area is {0:.2f}".format(3.14 * radius * radius))

class ConsoleInteractionTests(TestCase):

    def setUp(self):
        self.consoleMock = mock()
        self.shapeInput = ShapeInput(self.consoleMock)
    
    def testPrintsMessageWhenAskingForShape(self):
        self.shapeInput.askForShape()
        verify(self.consoleMock).printMessage(self.shapeInput.message)
        
    def testRequestsInputFromConsole(self):
        self.shapeInput.askForShape()
        verify(self.consoleMock).readString()

    def testAsksForRadiusIfCircle(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.circleShapeType)
        when(self.consoleMock).readFloat().thenReturn(100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.circleRadiusMessage)
        
    def testAsksForWidthIfRectangle(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.rectangleShapeType)
        when(self.consoleMock).readFloat().thenReturn(100).thenReturn(10)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.rectangleWidthMessage)
        
    def testAsksForHeightIfRectangle(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.rectangleShapeType)
        when(self.consoleMock).readFloat().thenReturn(100).thenReturn(10)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.rectangleHeightMessage)
        
    def testPrintsCorrectRectangleArea(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.rectangleShapeType)
        when(self.consoleMock).readFloat().thenReturn(100).thenReturn(100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Area is 10000.00")
        
    def testPrintsSecondCorrectRectangleArea(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.rectangleShapeType)
        when(self.consoleMock).readFloat().thenReturn(10).thenReturn(100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Area is 1000.00")
        
    def testPrintsCorrectCircleArea(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.circleShapeType)
        when(self.consoleMock).readFloat().thenReturn(100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Area is 31400.00")
