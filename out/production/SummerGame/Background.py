import pygame
import os


class Background:
    def __init__(self, image, height, width, screen):

        self.image = image
        self.height = height
        self.width = width
        self.screen = screen
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
    """credit to pygame download example"""


    def load_image(self,file):

        file = os.path.join(self.main_dir, 'data', file)
        try:
            surface = pygame.image.load(file)
        except pygame.error:
         raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
        return surface.convert()


    def draw_background(self, xpos, ypos):
        self.screen.blit(self.load_image(self.image), xpos, ypos)

