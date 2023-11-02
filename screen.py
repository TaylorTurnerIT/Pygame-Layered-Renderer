import pygame
import logging
from math import floor

pygame.init()

# VIEW OBJECT
# TODO: Create an object to store draw methods w/ preferred layer

# This system is a layer based approach, with only one draw per layer. Perhaps in the future I can investigate parallel programming which seems like the best approach to drawing two things on the same layer
class Screen:
    # Stores the object and their layer
    class Node:
        def __init__(self, objectToDraw, preferredLayer):
            self.obj = objectToDraw
            self.layer = preferredLayer
        # overload < operator
        def __lt__(self, other):
            return self.layer < other.layer

    # Input of to caption text, horizontal width, vertical height
    def __init__(self, captionInput = "My Program", screenWidthInput = floor(pygame.display.Info().current_w/2), screenHeightInput = floor(pygame.display.Info().current_h/2)):
        # Defines the pygame canvas
        self.canvas = pygame.display.set_mode((screenWidthInput, screenHeightInput)) 
        # Stores all of the programs visual functions in order of layers
        self.drawMethods = []
        # Draws the caption in the top bar
        self.captionText = captionInput

    # Adds a draw function to the draw array, takes an input of an object
    def addDraw(self, objectToDraw, preferredLayer):
        self.newNode = self.Node(objectToDraw, preferredLayer)
        self.drawMethods.append(self.newNode)
        # Sorts the draw array by layer after new layer is added
        self.sort(self.drawMethods)

    # Externally accessible caption update
    def updateCaption(self, newCaption):
        self.captionText = newCaption
        pygame.display.set_caption(self.captionText)

    def sort(self, unsortedArray):
        array = unsortedArray
        i = 1
        while (i < len(array)):
            j = i
            while (j > 0 and array[j-1] > array[j]):
                dummy = array[j]
                array[j] = array[j-1]
                array[j-1] = dummy
                j -= 1
            i += 1

    # Primary screen update
    def draw(self):
        for x in range(0, len(self.drawMethods)):
            self.drawMethods[x].obj.draw(self.canvas)
        pygame.display.update()