import pygame
import numpy as np
from screen import *
  
pygame.init() 
  
exit = False
screen = Screen("Default Program")

# GAME LOOP
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    screen.draw()