# See https://sites.google.com/site/tddproblems/all-problems-1/Console-interaction for problem description
from unittest.case import TestCase
from mockito import *


class ShapeInput():

    message = "Shape: (C)ircle or (R)ectangle?"
    circleRadiusMessage = "Circle radius is: "
    rectangleWidthMessage = "Rectangle width is: "
    rectangleShapeType = 'R'
    circleShapeType = 'C'
    
    def __init__(self, console):
        self.console = console

    def askForShape(self):
        self.console.printMessage(self.message)
        shapeType = self.console.read()
        
        if shapeType == self.rectangleShapeType:
            self.console.printMessage(self.rectangleWidthMessage)

        if shapeType == self.circleShapeType:
            self.console.printMessage(self.circleRadiusMessage)

class ConsoleInteractionTests(TestCase):

    def setUp(self):
        self.consoleMock = mock()
        self.shapeInput = ShapeInput(self.consoleMock)
    
    def testPrintsMessageWhenAskingForShape(self):
        self.shapeInput.askForShape()
        verify(self.consoleMock).printMessage(self.shapeInput.message)
        
    def testRequestsInputFromConsole(self):
        self.shapeInput.askForShape()
        verify(self.consoleMock).read()

    def testAsksForRadiusIfCircle(self):
        when(self.consoleMock).read().thenReturn(self.shapeInput.circleShapeType)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.circleRadiusMessage)
        
    def testAsksForWidthIfRectangle(self):
        when(self.consoleMock).read().thenReturn(self.shapeInput.rectangleShapeType)
        
        self.shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(self.shapeInput.rectangleWidthMessage)