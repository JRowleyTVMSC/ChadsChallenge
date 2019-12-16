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


TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 45


camMoveSpeed = 5


IMAGEDICT = {'W' : pygame.image.load("baseWallBlock.png"),
             '_' : pygame.image.load("floorBlock.png"),
             'D' : pygame.image.load("deathBlock.png"),
             'C' : pygame.image.load("conveyorBelt.png"),
             'H' : pygame.image.load("hintBlock.png"),
             'K' : pygame.image.load("keyBlock.png")}


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


def main() :
    global FPSCLOCK, DISPLAYSURF, IMAGEDICT, COOLFONT, BASICFONT, CURRENTIMAGE

    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.dispaly.set_mode((WWIDTH,WHEIGHT))

    pygame.display.set_caption('game')
    COOLFONT - pygame.font.Font("VIDEOPHREAK.ttf", 40)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)

    IMAGEDICT = {'W': pygame.image.load("baseWallBlock.png"),
                 '_': pygame.image.load("floorBlock.png"),
                 'D': pygame.image.load("deathBlock.png"),
                 'C': pygame.image.load("conveyorBelt.png"),
                 'H': pygame.image.load("hintBlock.png"),
                 'K': pygame.image.load("keyBlock.png")}

    CURRENTIMAGE = 0
    levels = readLevelsFile("level1.txt")
    currentLevelIndex = 0
    while True:
            result = runLevel(levels, currentLevelIndex)

            if result in ('solved', 'next') :
                currentLevelIndex += 1
                if currentLevelIndex >= len(levels) :
                    currentLevelIndex = 0
            elif result == 'back' :
                currentLevelIndex -= 1
                if currentLevelIndex < 0 :
                    currentLevelIndex = len(levels) - 1
            elif result == 'reset' :
                pass

def runLevel(levels, levelNum) :

   global currentImage
   levelObj = levels[levelNum]
   mapNeedsRedraw = True
   levelSurf = BASICFONT.render('Level %s of %s' % (levelObj['levelNum'] + 1, totalNumOfLevels), 1, PBLUE)
   levelRect = levelSurf.get_rect()
   levelRect.bottomleft = (20, WHEIGHT - 35)
   mapWidth = len(mapObj) * TILEWIDTH
   mapHeight = (len(mapObj[0]) - 1) * (TILEHEIGHT - TILEFLOORHEIGHT) + TILEHEIGHT

    levelIsComplete = False

   cameraOffsetX = 0
   cameraOffsetY = 0

   cameraUp = False
   cameraDown = False
   cameraLeft = False
   cameraRight = False

    playing = True
    while playing :

        playerMoveTo = None
        keyPressed = False

        for event in pygame.event.get() :
            if event.type == QUIT :
                playing = False

            elif event.type == KEYDOWN :
                keyPressed = True
                if event.key == K_LEFT :
                    playerMoveTo = LEFT
                    cameraLeft = True
                elif event.key == K_RIGHT :
                    playerMoveTo = RIGHT
                    cameraRight = True
                elif event.key == K_UP :
                    playerMoveTo = UP
                    cameraUp = True
                elif event.key == K_DOWN :
                    playerMoveTo = DOWN
                    cameraDown = True

        if playerMoveTo != None and not levelIsComplete :
            moved = makeMove(mapObj, gameStateObj, playerMoveTo)


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

def clockScore() :
    FPSCLOCK.tick(FPS)
    alive = True
    score = 0
    trueScore = 150
    timeInt = int(pygame.time.get_ticks() / 1000)
    scoreStr = str(score)

    displayScore = COOLFONT.render(scoreStr, True, BLACK)
    while alive :
        score -= trueScore - timeInt

    INFOSURF.blit(displayScore, (40,40))

def drawBoard() :
    for x in range(0, WWIDTH,CELLSIZE) :
        pygame.draw.line(GAMESURF, DGRAY, (x, 0), (x, WHEIGHT))
    for y in range(0,WHEIGHT, CELLSIZE) :
        pygame.draw.line(GAMESURF, DGRAY, (0, y), (WWIDTH, y))


def parseThing() :
    levelString =  open("level1.txt", "r")
    chadBoard = []
    lineTarget = {1}
    for i, row in enumerate(open("level1.txt")) :
        if i in lineTarget :
            chadBoard.append(row)

    print(chadBoard)


def makeMove(levelObj, gameStateObj, playerMoteTo) :

    playerx, playery = gameStateObj['player']
    chips = gameStateObj['chips']

    if playerMoveTo == UP:
        xOffset = 0
        yOffset = -1
    elif playerMoveTo == RIGHT:
        xOffset = 1
        yOffset = 0
    elif playerMoveTo == DOWN:
        xOffset = 0
        yOffset = 1
    elif playerMoveTo == LEFT:
        xOffset = -1
        yOffset = 0

def boardBuild(filename) :
    levelFile = open("level1.txt", 'r')
    content = levelFile.readlines() + ['\r\n']
    levelFile.close()

    levels = []
    levelNum = 0
    levelTextLines = []
    levelObj = []
    for lineNum in range(len(content)) :
        line = content[lineNum].rstrip('\r\n')

        if line != '' :
            levelTextLines.append(line)
        elif line == '' and len(levelTextLines) > 0 :
            maxWidth = -1
            for i in range(len(levelTextLines)) :
                if len(levelTextLines[i]) > maxWidth :
                    maxWidth = len(levelTextLines[i])
            for x in range(len(levelTextLines[0])) :
                levelObj.append([])
            for y in range(len(levelTextLines[0])) :
                for x in range(maxWidth) :
                    levelObj[x].append(levelTextLines[y][x])





main()