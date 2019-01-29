from pygame.math import Vector2

from settings import *


vec=pygame.math.Vector2

class Character(pygame.sprite.Sprite):

    pos: Vector2

    def __init__(self, x, y,platforms):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.jump_image = []
        self.load_idle()
        self.run_images = []
        self.land_image = []
        self.load_run()
        self.jump_image.append(pygame.transform.scale(pygame.image.load('data/jump.png'),(90,90)))
        self.land_image.append(pygame.transform.scale(pygame.image.load('data/landing.png'),(90,90)))
        self.platforms = platforms
        self.index = 0
        self.image = self.images[self.index]
        self.idle=True
        self.run=False
        self.run_index=0
        self.run_image=self.run_images[self.run_index]
        self.direction="RIGHT"
        self.jump=True
        self.rect = self.image.get_rect()
        self.rect.center = (0,250)
        self.pos = vec(0,250)
        self.vel = vec(0,0)
        self.acc = vec (0,0)
        self.y = self.pos.y
        self.j = 0



    def image_scroll(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        if clock.get_time() % 3 == 0:
            if(self.idle==True):
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
            if(self.run==True):
                self.run_index += 1
                if self.run_index >= len(self.run_images):
                    self.run_index = 0
                self.run_image = self.run_images[self.run_index]


    def update(self):

        if(self.idle==True):
            if(self.direction=="LEFT"):
                screen.blit(pygame.transform.flip(self.image,True,False), (self.pos.x, self.pos.y -45))
                self.image_scroll()

            else:
                screen.blit(self.image, (self.pos.x, self.pos.y-45))
                self.image_scroll()

        if(self.run==True):
            if(self.direction=="LEFT"):
                screen.blit(pygame.transform.flip(self.run_image,True,False), (self.pos.x, self.pos.y-45))
                self.image_scroll()
            else:
                screen.blit(self.run_image, (self.pos.x, self.pos.y-45))
                self.image_scroll()
            self.run = False
            self.idle = True
        if(self.jump==True):
            if(self.direction=="LEFT"):
                if self.y > self.pos.y:
                    screen.blit(pygame.transform.flip(self.jump_image[0],True,False), (self.pos.x, self.pos.y-45))
                else:
                    screen.blit(pygame.transform.flip(self.land_image[0],True,False), (self.pos.x, self.pos.y-45))
                self.image_scroll()

            else:
                if self.y > self.pos.y:
                    screen.blit(self.jump_image[0], (self.pos.x, self.pos.y-45))
                else:
                    screen.blit(self.land_image[0], (self.pos.x, self.pos.y-45))
                self.image_scroll()


        hits = pygame.sprite.spritecollide(self, self.platforms, False)

        if hits:
            self.jump = False
            self.idle = True

            self.pos.y = (hits[0].rect.top-hits[0].rect.height/2)
            print(hits[0].rect.top)
            self.vel.y = 0














    def move(self):
        self.acc = vec(0, PLAYER_GRAV)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.jump == False:
                self.run = True
                self.idle = False
            self.direction = "LEFT"
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            if self.jump == False:
                self.run = True
                self.idle = False
            self.direction = "RIGHT"
            self.acc.x = PLAYER_ACC

        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos


    def jump_up(self):
        if (self.j == 0 or self.j == 1):
            self.run = False
            self.idle = False
            self.jump = True
            print("JUMP")
            self.vel.y = -40







            





    def load_run(self):
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_1_delay-0.1s.gif'),(90,90)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_2_delay-0.1s.gif'),(90,90)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_3_delay-0.1s.gif'),(90,90)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_4_delay-0.1s.gif'),(90,90)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_5_delay-0.1s.gif'),(90,90)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_6_delay-0.1s.gif'),(90,90)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_7_delay-0.1s.gif'),(90,90)))
    def load_idle(self):
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_00_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_01_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_02_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_03_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_04_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_05_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_06_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_07_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_08_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_09_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_10_delay-0.1s.gif'),(90,90)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_11_delay-0.1s.gif'),(90,90)))