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
testRect = Node(0, 0, 100, 100, (0, 155, 0)) # Green rectangle
testRect2 = Node(50, 50, 100, 100, (0, 0, 155)) # Blue rectangle

screen.addDraw(testRect, 5)
screen.addDraw(testRect2, 2)

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