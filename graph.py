import pygame
import numpy as np
from screen import *

# INIT
pygame.init() # Pygame init
screen = Screen("Default Program") # Screen init
exit = False # Game loop exit condition

# Node class for graph
class Node:
    def __init__(self, x, y, width, height, color):
        # Visual properties
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.c = color
        # Data properties
        self.neighbors = []
        self.data = None


    def draw(self, canvas):
        pygame.draw.rect(canvas, self.c, pygame.Rect(self.x, self.y, self.w, self.h))


# GAME VARIABLES
testRect = Node(0, 0, 100, 100, (0, 155, 0))
testRect2 = Node(50, 50, 100, 100, (0, 0, 155))

screen.addDraw(testRect, 1)
screen.addDraw(testRect2, 0)

# GAME LOOP
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    screen.draw()

# QUIT
pygame.quit()