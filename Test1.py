import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
FRAME_RATE = 30
BG_COLOUR = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ENEMY_VELOCITY = 1

SBWIDTH = 60
SBHEIGHT = 50


ThorImg = pygame.image.load('Thor.png') # loading all the game images. :)
Stu1Img = pygame.image.load('student1.png')
Stu2Img = pygame.image.load('student2.png')
Stu3Img = pygame.image.load('student3.png')
Stu4Img = pygame.image.load('student4.png')
Stu5Img = pygame.image.load('student5.png')


DISPLAYSURF = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('GAME NAME HERE PLZ')


DISPLAYSURF.fill(BG_COLOUR)

class THOR (pygame.sprite.Sprite): #player
        def __init__ (self):
            pygame.sprite.Sprite.__init__(self)
            self.image = ThorImg 
            self.rect = self.image.get_rect()
            self.blindrect = pygame.Rect ((self.rect.top, self.rect.left), (self.rect.width, self.rect.height))

        def update(self):
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            self.rect.x = x
            self.rect.y = y
            self.blindrect.x = self.rect.x
            self.blindrect.y = self.rect.y


# A class for enemies that also extends Sprite in a slightly different way
class Enemy(pygame.sprite.Sprite):

    dx = 0;
    dy = ENEMY_VELOCITY;
    
    # initialization
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.type = randint(1,10)
        self.rect = self.image.get_rect()
        self.rect.x =  randint(100, 500)
        self.rect.y =-15
        if self.type // 2:
                self.image.fill(RED)
        else:
                self.image.fill(BLUE)
    
    # update this sprite's position
    def update(self):
        self.rect.x += self.dx;
        self.rect.y += self.dy;
        
        # if it goes off the screen, start over at the top
        if self.rect.y > 400:
            self.rect.x =  randint(100, 500)
            self.rect.y =-15
        
"""

class STUDENT: # enemies
class CODE: # the projectiles shot by the students
"""
allSprites = pygame.sprite.Group()
Thor = THOR()
enemy = Enemy()
allSprites.add(enemy)
allSprites.add(Thor)


while True: #this is the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.mouse.set_visible(False)
    DISPLAYSURF.fill(BG_COLOUR)
    DISPLAYSURF.blit(DISPLAYSURF, (0, 0))    
    allSprites.update()
    allSprites.draw(DISPLAYSURF)
    pygame.display.update ((Thor.rect, Thor.blindrect))
    DISPLAYSURF.blit(Stu1Img, [0, 0])# Need to address repeating code.
    DISPLAYSURF.blit(Stu2Img, [100, 0])
    DISPLAYSURF.blit(Stu3Img, [200, 0])
    DISPLAYSURF.blit(Stu4Img, [300, 0])
    DISPLAYSURF.blit(Stu5Img, [400, 0])
    pygame.display.update()

