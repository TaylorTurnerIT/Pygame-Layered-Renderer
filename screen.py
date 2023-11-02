import pygame
import logging
from math import floor

pygame.init()

# VIEW OBJECT
# TODO: Create an object to store draw methods w/ preferred layer

# This system is a layer based approach, with only one draw per layer. Perhaps in the future I can investigate parallel programming which seems like the best approach to drawing two things on the same layer
class Screen:
    # Input of to caption text, horizontal width, vertical height
    defaultCaption = "Default Program"
    defaultScreenWidth = floor(pygame.display.Info().current_w/2)
    defaultScreenHeight = floor(pygame.display.Info().current_h/2)

    def __init__(self, captionInput = defaultCaption, screenWidthInput = defaultScreenWidth, screenHeightInput = defaultScreenHeight.current_h/2):
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
        # TODO: Measure performance impact of sorting every time a new draw is added
        self.drawMethods = self.sort(self.drawMethods) 

    # Externally accessible caption update
    def updateCaption(self, newCaption):
        self.captionText = newCaption
        pygame.display.set_caption(self.captionText)

    # Sorts the draw array by layer
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
        return array

    # Primary screen update
    def draw(self):
        for x in range(0, len(self.drawMethods)):
            self.drawMethods[x].obj.draw(self.canvas)
        pygame.display.update()

    # Optional toggles
    def toggleGrid(self):
        if(self.grid == True):
            self.grid = False
        else:
            self.grid = True

    def toggleFPS(self):
        if(self.fps == True):
            self.fps = False
        else:
            self.fps = True

    # Stores the object and their layer
    class Node:
        def __init__(self, objectToDraw, preferredLayer, visible = True):
            self.obj = objectToDraw
            self.layer = preferredLayer
            self.visible = visible
        # overload < operator
        def __lt__(self, other):
            return self.layer < other.layer
    # Stores the grid properties
    class Grid:
        def __init__(self, gridSize = 20, color = "light grey"):
            self.gridSize = gridSize
            self.color = color
        def draw(self, canvas):
            for x in range(0, canvas.get_width(), self.gridSize):
                pygame.draw.line(canvas, self.color, (x, 0), (x, canvas.get_height()))
            for y in range(0, canvas.get_height(), self.gridSize):
                pygame.draw.line(canvas, self.color, (0, y), (canvas.get_width(), y))
    # Stores the FPS properties
    class FPS:
        def __init__(self, color = "yellow"):
            self.color = color
        def draw(self, canvas):
            self.font = pygame.font.SysFont("Arial", 12)
            self.text = self.font.render(str(int(pygame.time.Clock().get_fps())), True, self.color)
            canvas.blit(self.text, (0, 0))

