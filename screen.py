import pygame
import logging
from math import floor

# VIEW OBJECT
# TODO: Create an object to store draw methods w/ preferred layer

# This system is a layer based approach, with only one draw per layer. Perhaps in the future I can investigate parallel programming which seems like the best approach to drawing two things on the same layer
class Screen:
    # Stores the object and their layer
    class Node:
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
    def addDraw(self, objectToDraw, preferredLayer):
        self.newNode = self.Node(objectToDraw, preferredLayer)
        self.draw.append(self.newNode)

    # Externally accessible caption update
    def updateCaption(self, newCaption):
        self.captionText = newCaption
        pygame.display.set_caption(self.captionText)

    def sort(self, unsortedArray):
        array = unsortedArray
        i = 1
        while (i < array.length):
            j = i
            while (j > 0 and array[j-1] > array[j]):
                dummy = array[j]
                array[j] = array[j-1]
                array[j-1] = dummy
                j -= 1
            i += 1

    # Primary screen update
    def draw(self):
        # Sorts the list by layer each iteration, probably inefficient. TODO: Make better solution
        self.sort(self.drawMethods)
        for x in range(0, self.drawMethods.size):
            self.drawMethods.pop().draw(self.canvas)
        pygame.display.update()