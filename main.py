import pygame
import random

'INIT'

pygame.init()
pygame.display.init()
pygame.font.init()

'CONSTANT'

# DELAY
delay = 30

# RUN LOOP
GameRun = True

# WINDOW
WinWidth, WinHeight = 1280, 1024
window = pygame.display.set_mode((WinWidth, WinHeight))

# ME
MeWidth, MeHeight = WinWidth//70, WinHeight//70
MeX, MeY = WinWidth//2, WinHeight//2
x, y = MeX, MeY
me = pygame.Surface((MeWidth, MeHeight))
me.fill((63,81,181))
MeSpeed = 5

# TEXT
FontXY = pygame.font.Font(None , 22)
FontX, FontY = 0, 0
TextCoordinates = FontXY.render('x : ' + str(MeX) + ' , y : ' + str(MeY) , True , (0,0,0))

#TREE
TreeData = []
TreeWidth, TreeHeight = WinWidth//55, WinHeight//50

#FIELD
MaxX, MaxY = 2*WinHeight, 2*WinWidth
MinX, MinY = -WinHeight, -WinWidth
LastChunk = [MeX, MeY]

'FUNCTIONS'

#TREE
def spawnTree(max, min):
    x1, y1 = max[0], max[1]
    x2, y2 = min[0], min[1]
    count = random.randint((x1-x2)//89 , (x1-x2)//79)
    for i in range(count):
        x = random.randint(x2,x1)
        y = random.randint(y2,y1)
        tree = pygame.Surface((TreeWidth, TreeHeight))
        tree.fill((62,39,35))
        window.blit(tree, (x,y))
        info ={'tree': tree,
               'pos': [x,y]}
        TreeData.append(info)

def supportTree():
    for info in TreeData:
        x, y = info['pos'][0], info['pos'][1]
        tree = info['tree']
        window.blit(tree , (x,y))

def moveTree(axis, speed):
    for info in TreeData:
        if axis == 'x':
            info['pos'][0] += speed
        else:
            info['pos'][1] += speed


def Transport(value , axis):
    global x, y, MaxX, MaxY, MinX, MinY, LastChunk
    if axis == 'x':
        if value == '+':
            x += MeSpeed
            moveTree(axis, -MeSpeed)
            if x > MaxX:
                MaxX = x
        else:
            x -= MeSpeed
            moveTree(axis, MeSpeed)
            if x < MinX:
                MinX = x
    else:
        if value == '+':
            y += MeSpeed
            moveTree(axis, -MeSpeed)
            if y > MaxY:
                MaxY = y
        else:
            moveTree(axis, MeSpeed)
            y -= MeSpeed
            if y < MinY:
                MinY = y
    if abs(LastChunk[0] - x) == WinHeight:
        LastChunk[0] = x
        #swapChunk()
    if abs(LastChunk[1] - y) == WinWidth:
        LastChunk[1] = y
        #swapChunk()
    return FontXY.render('x : ' + str(x) + ' , y : ' + str(y) , True , (0,0,0))


'MAINLOOP'

spawnTree([MaxX, MaxY] , [MinX, MinY])
while GameRun:
    supportTree()
    pygame.display.update()
    pygame.time.delay(delay)
    window.fill((46,125,50))
    window.blit(me, (MeX, MeY))
    window.blit(TextCoordinates, (FontX, FontY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRun = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        value, axis = '-', 'y'
        TextCoordinates = Transport(value, axis)
    if keys[pygame.K_d]:
        value, axis = '+', 'x'
        TextCoordinates = Transport(value, axis)
    if keys[pygame.K_s]:
        value, axis = '+', 'y'
        TextCoordinates = Transport(value, axis)
    if keys[pygame.K_a]:
        value, axis = '-', 'x'
        TextCoordinates = Transport(value, axis)


