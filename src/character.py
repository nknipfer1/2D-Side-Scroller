import pygame

vec=pygame.math.Vector2

class Character(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Character, self).__init__()
        self.images = []
        self.jump_image = []
        self.load_idle()
        self.run_images = []
        self.load_run()
        self.jump_image.append(pygame.transform.scale(pygame.image.load('data/jump.png'),(125,125)))
        self.index = 0
        self.image = self.images[self.index]
        self.counter=0
        self.action = " "
        self.idle=True
        self.run=False
        self.run_index=0
        self.run_image=self.run_images[self.run_index]
        self.direction="RIGHT"
        self.v = 8
        self.m = 2
        self.jump=False
        self.landing=False
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y = y
        self.vel = vec(0,225)
        self.change=False

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        if(self.counter==18):
            self.counter=0
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

        else:
            self.counter+=1
    def move(self):
        self.idle=False
        self.run=True

        if (self.direction=="LEFT"):
            self.vel = [-8,0]
        if (self.direction=="RIGHT"):
            self.vel = [8,0]
        # apply friction
        # equations of motion
        self.rect.x += self.vel[0]



            

        print(self.acc,self.vel)
    def jump_up(self):
        # jump only if standing on a platfor
        self.vel[1] = -20
        self.move()

    def load_run(self):
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_1_delay-0.1s.gif'),(125,125)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_2_delay-0.1s.gif'),(125,125)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_3_delay-0.1s.gif'),(125,125)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_4_delay-0.1s.gif'),(125,125)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_5_delay-0.1s.gif'),(125,125)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_6_delay-0.1s.gif'),(125,125)))
        self.run_images.append(pygame.transform.scale(pygame.image.load('data/Run/frame_7_delay-0.1s.gif'),(125,125)))
    def load_idle(self):
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_00_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_01_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_02_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_03_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_04_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_05_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_06_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_07_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_08_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_09_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_10_delay-0.1s.gif'),(125,125)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/Idle/frame_11_delay-0.1s.gif'),(125,125)))