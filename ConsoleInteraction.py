# See https://sites.google.com/site/tddproblems/all-problems-1/Console-interaction for problem description
from unittest.case import TestCase
from mockito import *


class ShapeInput():

    message = "Shape: (C)ircle or (R)ectangle?"
    
    def __init__(self, console):
        self.console = console

    def askForShape(self):
        self.console.printMessage(self.message)
        self.console.read()

class ConsoleInteractionTests(TestCase):

    def setUp(self):
        self.consoleMock = mock()
    
    def testPrintsMessageWhenAskingForShape(self):
        shapeInput = ShapeInput(self.consoleMock)
        
        shapeInput.askForShape()
        
        verify(self.consoleMock).printMessage(shapeInput.message)
        
    def testRequestsInputFromConsole(self):
        shapeInput = ShapeInput(self.consoleMock)
        
        shapeInput.askForShape()
        
        verify(self.consoleMock).read()