import pygame
from Background import Background
from character import Character
import sys
from PIL import Image


"""
intialize pygame
"""

pygame.init()
im = Image.open('/home/nathan/IdeaProjects/SummerGame/src/data/marsh.gif')
width, height = im.size
screen = pygame.display.set_mode([width,height])



background=Background("countryfield.png",width,height,screen)
character=Character(0,225)
guy = pygame.sprite.Group(character)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
           if(character.jump==False):
                character.idle=True
                character.run=False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        character.acc = (0.5,0.8)
        character.direction="RIGHT"
        character.move()

    if keys[pygame.K_LEFT]:
        character.acc=(-0.5,0.8)
        character.direction="LEFT"
        character.move()

    if keys[pygame.K_UP]:
        character.acc=(0,0.8)
        character.jump_up()


    background.draw_background(0,0)

    if(character.idle==True):
        if(character.direction=="LEFT"):
            screen.blit(pygame.transform.flip(character.image,True,False), (character.rect.x, character.rect.y))
            character.update()

        else:
            screen.blit(character.image, (character.rect.x, character.rect.y))
            character.update()
    if(character.run==True):
        if(character.direction=="LEFT"):
            screen.blit(pygame.transform.flip(character.run_image,True,False), (character.rect.x, character.rect.y))
            character.update()
        else:
            screen.blit(character.run_image, (character.rect.x, character.rect.y))
            character.update()
    if(character.jump==True):
        if(character.direction=="LEFT"):
            screen.blit(pygame.transform.flip(character.jump_image[0],True,False), (character.rect.x, character.rect.y))
            character.idle=False
            character.update()
        else:
            screen.blit(character.jump_image[0], (character.rect.x, character.rect.y))
            character.idle=False
            character.update()
    pygame.display.flip()