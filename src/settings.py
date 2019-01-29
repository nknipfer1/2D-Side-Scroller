from PIL import Image
from Background import *

im = Image.open('/home/nathan/IdeaProjects/SummerGame/src/data/marsh.gif')
WIDTH, HEIGHT = im.size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background=Background("countryfield.png",WIDTH,HEIGHT,screen)

PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.6
clock = pygame.time.Clock()

