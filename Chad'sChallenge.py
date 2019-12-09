import pygame, random, sys, time
from pygame.locals import *
from pygame.sprite import *

# main board colors
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
DGRAY = (100, 100, 100)
LGRAY = (200, 200, 200)

# sprite and funtion item colors

ORANGE = (245, 140, 50)
PBLUE = (170, 230, 252)


# window related jazz

WWIDTH = 1366
WHEIGHT = 768
HALFHEIGHT = WHEIGHT / 2
HALFWIDTH = WWIDTH / 2
INFOCORNER = (WWIDTH - (WWIDTH / 4), 0)
INVCORNER = (WWIDTH - (WWIDTH / 4), (WHEIGHT - (WHEIGHT / 4)))


FPS = 30


wallBlock = pygame.image.load("baseWallBlock.png")
floorBlock = pygame.image.load("floorBlock.png")
deathBlock = pygame.image.load("deathBlock.png")
conveyorBlock = pygame.image.load("conveyorBelt.png")
hintBlock = pygame.image.load("hintBlock.png")
keyBlock = pygame.image.load("keyBlock.png")


LINENUMBER = 20

class Entity(Sprite) :
    def __init__(self, x, y, width, height) :
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#   CHECK HISTORY FOR WEBSITES USED. GOOD STACKOVERFLOW STUFF YOU FORGOT TO BOOKMARK YOU IDIOT

class BaseTile(Sprite) :
    def __init__(self, x, y, fileName, fileType) :

        self.image = pygame.image.load(fileName)
        self.rect = self.image.get_rect()

        self.bX = x
        self.bY = y

        self.fType = fileType

class wallBlock(BaseTile) :
    def __init__(self, bX, bY) :
        BaseTile.__init__(self, bX, bY, "baseWallBlock.png")

class floorBlock(BaseTile) :
    def __init__(self, bX, bY) :
        BaseTile.__init__(self, bX, bY, "floorBlock.png")

class deathBlock(BaseTile) :
    def __init__(self, bX, bY) :
        BaseTile.__init__(self, bX, bY, "deathBlock.png")

class conveyorBlock(BaseTile) :
    def __init__(self, bX, bY) :
        BaseTile.__init__(self, bX, bY, "conveyorBlock.png")

class hintBlock(BaseTile) :
    def __init__(self, bX, bY) :
        BaseTile.__init__(self, bX, bY, "hintBlock.png")
class keyBlock(BaseTile) :
    def __init__(self, bX, bY) :
        BaseTile.__init__(self, bX, bY, "keyBlock.png")



def main() :
    global FPSCLOCK, DISPLAYSURF, INFOSURF, COOLFONT, BASICFONT


    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WWIDTH, WHEIGHT))
    pygame.display.set_caption("It's Chad's Challenge baby!")
    COOLFONT = pygame.font.Font("VIDEOPHREAK.ttf", 40)
    INFOSURF = pygame.Surface((WHEIGHT / 2, 768))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    BOARDSPRITE = Group()
    bigClock(True)



    playing = True
    while playing:

        for event in pygame.event.get() :
            if event.type == QUIT :
                playing = False

        DISPLAYSURF.fill(BLACK)
        INFOSURF.fill(LGRAY)

        bigClock(False)

        DISPLAYSURF.blit(INFOSURF, (WWIDTH - (WWIDTH / 4) , 0))
        drawInv()

        pygame.display.update()
        FPSCLOCK.tick(FPS)



def bigClock(new) :
    FPSCLOCK.tick(FPS)
    timeNum = int(pygame.time.get_ticks() / 1000)
    timeStr = str(int(timeNum % 60))
    timeNum = timeNum - (timeNum % 60)
    minNum = 0
    while timeNum >= 60 :
        minNum += 1
        timeNum -= 60
    if len(timeStr) == 1 :
        timeStr = "0" + timeStr
    timeStr = str(minNum) + ":" + timeStr
    if new :
        timeStr = "0:00"
    timer = COOLFONT.render(timeStr, True, BLACK)
    INFOSURF.blit(timer, (20, 20))

# point of angery

def drawInv() :
    global INVSURF
    INVSURF = pygame.surface((WHEIGHT / 2, 200))
    INFOSURF.blit(INVSURF, (50 , 50))


def parseThing() :
    levelString =  open("level1.txt", "r")
    chadBoard = []
    lineTarget = {1}
    for i, row in enumerate(open("level1.txt")) :
        if i in lineTarget :
            chadBoard.append(row)

    print(chadBoard)



def boardBuild() :
    board = []
    blocks = pygame.sprite.Group()
    f = open("level1.txt", "r")
    line = f.readlines()
    f.close()
    for row in line :
        for column in row :
            if column == "w" :
                w = wallBlock(x, y)
                board.append(w)
                blocks.add()

main()