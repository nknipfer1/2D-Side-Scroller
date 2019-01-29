import os
import pygame


## new code below:

class Platform(pygame.sprite.Sprite):
# x location, y location, img width, img height, img file

    def __init__(self,x,y,imgw,imgh,i):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(i)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
