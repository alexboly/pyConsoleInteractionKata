# See https://sites.google.com/site/tddproblems/all-problems-1/Console-interaction for problem description
from mockito import *
from unittest.case import TestCase


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
            self.console.read()
            self.console.printMessage(self.rectangleHeightMessage)
            self.console.read()
            self.console.printMessage("Area is 10000")

        if shapeType == self.circleShapeType:
            self.console.printMessage(self.circleRadiusMessage)
            self.console.read()

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
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.circleRadiusMessage)

    def testReadsRadiusOfCircle(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.circleShapeType)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).read()
        
    def testAsksForWidthIfRectangle(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.rectangleShapeType)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.rectangleWidthMessage)
        
    def testAsksForHeightIfRectangle(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.rectangleShapeType)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.rectangleHeightMessage)
        
    def testReadsWidthAndHeightIfRectangle(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.rectangleShapeType)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock, 2).read()

    def testPrintsCorrectRectangleArea(self):
        when(self.consoleMock).readString().thenReturn(self.shapeInput.rectangleShapeType).thenReturn(100).thenReturn(100)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage("Area is 10000")
        