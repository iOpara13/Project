import pygame, sys
from pygame.locals import *
import random

pygame.init()
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
FRAME_RATE = 30
BG_COLOUR = (255, 255, 255)

SBWIDTH = 60
SBHEIGHT = 50


ThorImg = pygame.image.load('Thor.png') # loading all the game images. :)
BallImg = pygame.image.load('ball.png')
Stu1Img = pygame.image.load('student1.png')
Stu2Img = pygame.image.load('student2.png')
Stu3Img = pygame.image.load('student3.png')
Stu4Img = pygame.image.load('student4.png')
Stu5Img = pygame.image.load('student5.png')
Stu6Img = pygame.image.load('student6.png')
Stu7Img = pygame.image.load('student7.png')
Stu8Img = pygame.image.load('student8.png')
Stu9Img = pygame.image.load('student9.png')
Stu10Img = pygame.image.load('student10.png')

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
            if y > SCREEN_HEIGHT//2:
                self.rect.x = x
                self.rect.y = y
                self.blindrect.x = self.rect.x
                self.blindrect.y = self.rect.y

class BALL:
        def __init__(self, screen, x, y):
                self.screen = screen
                self.rect = pygame.Rect(0,0,0,0)
                self.image = BallImg
                self.rect.size = self.image.get_size()
                self.rect.center = (x, y)
                self.speed_x = 15
                self.speed_y = 15
                
        def draw(self):
                self.screen.blit(self.image,(self.rect.x,self.rect.y))

        def move(self):
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y

                if self.rect.left < 0 or self.rect.right > self.screen.get_size()[0]:
                    self.speed_x = -self.speed_x
                if self.rect.top < 0 or self.rect.bottom > self.screen.get_size()[1]:
                    self.speed_y = -self.speed_y
"""

class STUDENT: # enemies
class CODE: # the projectiles shot by the students
"""
Thor = THOR()

allSprites = pygame.sprite.Group(Thor)


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
    pygame.display.flip()
    pygame.display.update()

