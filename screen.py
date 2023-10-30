import pygame
import logging
from math import floor

# VIEW OBJECT
# TODO: Create an object to store draw methods w/ preferred layer

# This system is a layer based approach, with only one draw per layer. Perhaps in the future I can investigate parallel programming which seems like the best approach to drawing two things on the same layer
class Screen:
    # Stores the object and their layer
    class Module:
        def __init__(objectToDraw, preferredLayer):
            obj = objectToDraw
            layer = preferredLayer

    # Input of to caption text, horizontal width, vertical height
    def __init__(self, captionInput = "My Program", screenWidthInput = floor(pygame.display.Info.x/2), screenHeightInput = floor(pygame.display.Info.y/2)):
        # Defines the pygame canvas
        self.canvas = pygame.display.set_mode((screenWidthInput, screenHeightInput)) 
        # Stores all of the programs visual functions in order of layers
        self.drawMethods = []
        # Draws the caption in the top bar
        self.captionText = captionInput

    # Adds a draw function to the draw array, takes an input of an object
    def addDraw(self, objectToDraw):
        self.draw.append(objectToDraw)

    # Externally accessible caption update
    def updateCaption(self, newCaption):
        self.captionText = newCaption
        pygame.display.set_caption(self.captionText)

    # Primary screen update
    def draw(self):
        for x in range(0, self.drawMethods.size):
            self.drawMethods.pop().draw(self.canvas)
        pygame.display.update()