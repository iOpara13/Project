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

counter, text = 5, '5'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

ThorImg = pygame.image.load('Thor0.png') # loading all the game images. :)
BallImg = pygame.image.load('ball.png')
Stu1Img = pygame.image.load('student01.png')
Stu2Img = pygame.image.load('student02.png')
Stu3Img = pygame.image.load('student03.png')
Stu4Img = pygame.image.load('student04.png')
Stu5Img = pygame.image.load('student05.png')
Stu6Img = pygame.image.load('student06.png')
Stu7Img = pygame.image.load('student07.png')
Stu8Img = pygame.image.load('student08.png')
Stu9Img = pygame.image.load('student09.png')
BCodeImg = pygame.image.load('bcode.png')
GCodeImg = pygame.image.load('gcode.png')

DISPLAYSURF = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('GAME NAME HERE PLZ')

DISPLAYSURF.fill(BG_COLOUR)

enemies = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

class THOR (pygame.sprite.Sprite): #player
        def __init__ (self):
            super().__init__(self)
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

class STUDENT(pygame.sprite.Sprite):
        def __init__(self, img, x):
                super().__init__(self, enemies)
                self.image = img
                self.rect = self.image.get_rect()
                self.rect.top = 0
                self.rect.left = x
                DISPLAYSURF.blit(img, (x, 0))


Stu1 = STUDENT(Stu1Img, 0) #Creating all student instances of class
Stu2 = STUDENT(Stu2Img, (Stu1.rect.right + 5))
Stu3 = STUDENT(Stu3Img, (Stu2.rect.right + 5))
Stu4 = STUDENT(Stu4Img, (Stu3.rect.right + 5))
Stu5 = STUDENT(Stu5Img, (Stu4.rect.right + 5))
Stu6 = STUDENT(Stu6Img, (Stu5.rect.right + 5))
Stu7 = STUDENT(Stu7Img, (Stu6.rect.right + 5))
Stu8 = STUDENT(Stu8Img, (Stu7.rect.right + 5))
Stu9 = STUDENT(Stu9Img, (Stu8.rect.right + 5))

stucenter = (24, 77, 130, 183, 236, 289, 342, 395, 448) #x coordinate of student centres

class BCODE(pygame.sprite.Sprite):
        speedmax = 30
        
        def __init__(self, speed):
                super().__init__(self)
                self.image = bcode.png
                self.rect = self.image.get_rect()
                self.rect.center.x = random.choice(stucenter)
                self.rect.top = 48
                self.speed = random.randrange(15, speedmax)                                          edmax, 5)

        def move(self):
                self.rect.y += self.speed

        def draw(self):
                self.DISPLAYSURF.blit(self.image, (sel.rect.left, self.rect.top)
                

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
    enemies.update()
    enemies.draw(DISPLAYSURF)
    allSprites.update()
    allSprites.draw(DISPLAYSURF)
    pygame.display.update ((Thor.rect, Thor.blindrect))
    pygame.display.flip()
    pygame.display.update()


