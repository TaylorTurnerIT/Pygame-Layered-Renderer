import pygame

# VIEW OBJECT
# TODO: Create an object to store draw methods w/ preferred layer
class Screen:
    class drawModule:
        def __init__(objectToDraw, preferredLayer, layerCount):
            drawObject = objectToDraw
            drawObject = preferredLayer

    # Input of to caption text, horizontal width, vertical height
    def __init__(self, captionInput = "My Program", screenWidthInput = pygame.display.Info.x/2, screenHeightInput = pygame.display.Info.y/2):
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

    def draw(self):
        for x in range(0, self.drawMethods.size):
            self.drawMethods[x].draw(self.canvas)
        pygame.display.update() 