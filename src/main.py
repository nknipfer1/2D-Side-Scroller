import sys

from character import Character
from platforms import *
from settings import *

"""
intialize pygame
"""

pygame.init()

platform1 = Platform(0,388,156,27,'data/groundtile.png')
platform2 = Platform(156,388,156,27,'data/groundtile.png')
platform3 = Platform(312,388,156,27,'data/groundtile.png')
platform4 = Platform(468,388,156,27,'data/groundtile.png')
platform5 = Platform(624,388,156,27,'data/groundtile.png')
platform6 = Platform(780,388,156,27,'data/groundtile.png')
platform7 = Platform(936,388,156,27,'data/groundtile.png')
platform8 = Platform(468,210,156,27,'data/groundtile.png')

platforms = pygame.sprite.Group()

platforms.add(platform1)
platforms.add(platform2)
platforms.add(platform3)
platforms.add(platform4)
platforms.add(platform5)
platforms.add(platform6)
platforms.add(platform7)
platforms.add(platform8)

character = Character(20,245,platforms)
player =pygame.sprite.Group()
player.add(character)


while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN  and event.key == pygame.K_UP:
                character.jump_up()




    screen.fill((0,0,0))
    platforms.draw(screen)
    character.move()
    character.update()






    pygame.display.flip()
