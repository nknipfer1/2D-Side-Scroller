import pygame
from PIL import Image
from Background import Background

class Character(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Character, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('data/Idle/frame_00_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_01_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_02_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_03_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_04_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_05_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_06_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_07_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_08_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_09_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_10_delay-0.1s.gif'))
        self.images.append(pygame.image.load('data/Idle/frame_11_delay-0.1s.gif'))
        self.x=x
        self.y = y
        self.index = 0
        self.image = self.images[self.index]
        self.counter=0
        self.rect.x=x;
        self.rect.y=y;

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        if(self.counter==18):
            self.counter=0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        else:
            self.counter+=1
    def move(self):