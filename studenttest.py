import pygame, sys
from pygame.locals import *
import random

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (224, 224, 224)
GREEN = (0, 204, 0)
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
FRAME_RATE = 30
BG_COLOUR = (WHITE)
CLOCK = pygame.time.Clock()
fontsize = SCREEN_HEIGHT // 20
fontObj = pygame.font.Font('bitwise.ttf', fontsize)

SBWIDTH = 60
SBHEIGHT = 50

HUDlength = int(fontsize + 5)


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
#GCodeImg = pygame.image.load('gcode.png')

DISPLAYSURF = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('GAME NAME HERE PLZ')

HUD = pygame.Surface((SCREEN_WIDTH, HUDlength))
HUD.fill(GREY)
ybound = SCREEN_HEIGHT - 30

DISPLAYSURF.fill(BG_COLOUR)

enemies = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

class THOR (pygame.sprite.Sprite): #player
        def __init__ (self):
            pygame.sprite.Sprite.__init__(self, allSprites)
            self.image = ThorImg 
            self.rect = self.image.get_rect()
            self.blindrect = pygame.Rect ((self.rect.top, self.rect.left), (self.rect.width, self.rect.height))

        def update(self):
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if x < 0:
                self.rect.x = 0
            elif x > (SCREEN_WIDTH - self.rect.width):
                self.rect.x = SCREEN_WIDTH - self.rect.width
            elif y < 48:
                self.rect.y = 48
            elif y > (ybound - self.rect.height):
                self.rect.y = (ybound - self.rect.height)
            else:
                self.rect.x = x
                self.rect.y = y
                self.blindrect.x = self.rect.x
                self.blindrect.y = self.rect.y

class STUDENT(pygame.sprite.Sprite):
        def __init__(self, img, x):
                pygame.sprite.Sprite.__init__(self, enemies, allSprites)
                self.image = img
                self.rect = self.image.get_rect()
                self.rect.top = 0
                self.rect.left = x
                DISPLAYSURF.blit(img, (x, 0))

Stu1 = STUDENT(Stu1Img, 10) #Creating all student instances of class
Stu2 = STUDENT(Stu2Img, (Stu1.rect.right + 5))
Stu3 = STUDENT(Stu3Img, (Stu2.rect.right + 5))
Stu4 = STUDENT(Stu4Img, (Stu3.rect.right + 5))
Stu5 = STUDENT(Stu5Img, (Stu4.rect.right + 5))
Stu6 = STUDENT(Stu6Img, (Stu5.rect.right + 5))
Stu7 = STUDENT(Stu7Img, (Stu6.rect.right + 5))
Stu8 = STUDENT(Stu8Img, (Stu7.rect.right + 5))
Stu9 = STUDENT(Stu9Img, (Stu8.rect.right + 5))

stucenter = (Stu1.rect.centerx, Stu2.rect.centerx, Stu3.rect.centerx, Stu4.rect.centerx, Stu5.rect.centerx,
             Stu6.rect.centerx, Stu7.rect.centerx, Stu8.rect.centerx, Stu9.rect.centerx) #x coordinate of student centres

class BCODE(pygame.sprite.Sprite):
        def __init__(self, speed):
            pygame.sprite.Sprite.__init__(self, allSprites, projectiles)
            self.image = BCodeImg
            self.rect = self.image.get_rect()
            self.rect.centerx = random.choice(stucenter)
            self.rect.top = 48
            self.speed = speed

        def update(self):
            self.rect.y += self.speed
            if self.rect.y > (ybound - self.rect.height):
                self.kill()




Thor = THOR()

def game_intro(): #Intro Screen For Game
    intro = True
    introtext = "Help Thor Dodge His Students Terrible Code And Pick Up Good Code!"

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.fill(WHITE)
        introfont = pygame.font.Font('arcadeclassic.ttf', 115)
        welcome = introfont.render(introtext, True, GREEN, GREY)
        welcomerect = welcome.get_rect()
        welcomerect.rect.center = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
        DISPLAYSURF.blit(welcome, welcomerect)
        pygame.display.update()
        CLOCK.tick(15)


def firerate(currentlevel): #creates instances of bcode, delay and speed is based on the current level
    global projectiles
    maxadj = currentlevel * 150 #adjusts the max shot delay based on level
    minadj = currentlevel * 50 #adjusts the min shot delay based on level
    speedadj = currentlevel * 6 #adjusts bullet speed based on level
    mindelay = 1000 - minadj #decreases min delay based on level
    maxdelay = 3000 - maxadj # decreases max delay based on level
    maxspeed = 10 + speedadj
    if currentlevel == 1:
        mindelay = 1000
        maxdelay = 3000
        maxspeed = 20
    elif currentlevel > 10:
        mindelay = 500
        maxdelay = 1500
        maxspeed = 50
    codespeed = random.randrange(5, maxspeed)
    bullet = BCODE(codespeed)
    timecheck = CLOCK.get_time()
    delay = random.randrange(mindelay, maxdelay)
    if len(projectiles) < 20:
        if timecheck >= delay:
            bullet

def lives(chances): #collects the amount of lives
    lifeObj = fontObj.render(("Lives: %d" % (chances)), True, GREEN, GREY)
    lifeRectObj = lifeObj.get_rect()
    lifeRectObj.left = 5
    lifeRectObj.bottom = 30
    HUD.blit(lifeObj, lifeRectObj)

def score(count): #collects the amount of bcode dodged
    pointObj = fontObj.render(("Points: %d" % (count)), True, GREEN, GREY)
    pointRectObj = pointObj.get_rect()
    pointRectObj.left = 140
    pointRectObj.bottom = 30
    HUD.blit(pointObj, pointRectObj)

def lvlcount(progress):
    lvlObj = fontObj.render(("Level: %d" % (progress)), True, GREEN, GREY)
    lvlRectObj = lvlObj.get_rect()
    lvlRectObj.left = 350
    lvlRectObj.bottom = 30
    HUD.blit(lvlObj, lvlRectObj)

def game_loop():
    life = 3
    lvl = 1
    points = 0
    while True: #this is the main game loop
        CLOCK.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.mouse.set_visible(False)
        DISPLAYSURF.fill(BG_COLOUR)
        DISPLAYSURF.blit(DISPLAYSURF, (0, 0))
        DISPLAYSURF.blit(HUD, (0, 470))
        lives(life)
        score(points)
        lvlcount(lvl)
        firerate(lvl)
        allSprites.update()
        allSprites.draw(DISPLAYSURF)
        pygame.display.update ((Thor.rect, Thor.blindrect))
        pygame.display.flip()
        pygame.display.update()

#game_intro()
game_loop()
pygame.quit()
quit()
