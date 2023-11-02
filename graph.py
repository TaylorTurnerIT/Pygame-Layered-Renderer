import pygame
import numpy as np
from screen import *

# INIT
pygame.init() # Pygame init
screen = Screen("Default Program") # Screen init
exit = False # Game loop exit condition

# Node class for graph
class Square:
    def __init__(self, x, y, width, height, color):
        # Visual properties
        self.vector = pygame.Vector2(x,y) # Top left
        self.origin = pygame.Vector2(x+width/2,y+height/2) # Center
        self.size = pygame.Vector2(width, height)
        self.c = color
        # Data properties
        self.neighbors = []
        self.data = None

    def addNeighbor(self, neighborInput):
        # Check if it exists already, else append
        if (self.neighbors.count(neighborInput) == 0):
            self.neighbors.append(neighborInput)

    def removeNeighbor(self, neighborInput):
        # Chef if it exists, then delete
        if (self.neighbors.count(neighborInput) != 0):
            self.neighbors.remove(neighborInput)

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.c, pygame.Rect(self.vector, self.size))
        for neighbor in self.neighbors:
            startPos = self.origin
            endPos = neighbor.origin
            pygame.draw.line(canvas, "black", startPos, endPos, 1)


# GAME OBJECTS
testRect = Square(0, 0, 100, 100, "Dark Green") # Green rectangle
testRect2 = Square(378, 483, 100, 100, "Dark Blue") # Blue rectangle

screen.addDraw(testRect, 5)
screen.addDraw(testRect2, 2)
testRect.addNeighbor(testRect2)

# GAME LOOP
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        # Key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit = True
            if event.key == pygame.K_g:
                screen.toggleGrid()
            if event.key == pygame.K_f:
                screen.toggleFPS()

    
    screen.draw()

# QUIT
pygame.quit()