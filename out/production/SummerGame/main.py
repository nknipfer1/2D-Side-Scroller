import pygame
from Background import Background
import sys
from PIL import Image

import os
"""
intialize pygame
"""

pygame.init()
im = Image.open('/home/nathan/IdeaProjects/SummerGame/src/data/country field.png')
width, height = im.size
screen = pygame.display.set_mode([600, 500])


background=Background("countryfield.png",500,600,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for y in range(6):
        for x in range(5):
            background.draw_background(x*100, y*100)

    pygame.display.flip()