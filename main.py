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
MaxX, MaxY = 2*WinWidth, 2*WinHeight
MinX, MinY = -WinWidth, -WinHeight
LastChunk = [MeX, MeY]
ChunkData = [[WinWidth//2, WinHeight//2]]

'FUNCTIONS'

#TREE
def spawnTree(max, min):
    x1, y1 = max[0], max[1]
    x2, y2 = min[0], min[1]
    count = random.randint((x1-x2)//30 , (x1-x2)//20)
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

#ME
def Transport(value, axis):
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
    if abs(LastChunk[0] - x) > WinWidth:
        if LastChunk[0]>x:
            token = '-'
        else:
            token = '+'
        LastChunk[0] = x
        swapChunk('x', token, LastChunk)
    if abs(LastChunk[1] - y) > WinHeight:
        if LastChunk[1]>y:
            token = '-'
        else:
            token = '+'
        LastChunk[1] = y
        swapChunk('y', token, LastChunk)
    return FontXY.render('x : ' + str(x) + ' , y : ' + str(y) , True , (0,0,0))

def Destroy(Mex, Mey):
    for info in TreeData:
        TreeX, TreeY = info['pos'][0], info['pos'][1]
        if abs(Mex - TreeX) <= TreeWidth+10 and abs(Mey - TreeY) <= TreeHeight+10:
            TreeData.remove(info)

def Check(MeX, MeY, TreeData, MeSpeedX, MeSpeedY):
    k  = 0
    for info in TreeData:
        TreeX, TreeY = info['pos'][0], info['pos'][1]
        if MeX > TreeX and MeSpeedX < 0 or \
                MeX < TreeX and MeSpeedX > 0 or \
                        MeY < TreeY and MeSpeedY > 0 or \
                                MeY > TreeY and MeSpeedY < 0:
            if abs(MeX - TreeX) <= TreeWidth and abs(MeY - TreeY) <= TreeHeight:
                k = 1
    if k == 1:
        return False
    else:
        return True
#CHUNK
def swapChunk(axis, value, LastChunk):
    if LastChunk not in ChunkData:
        ChunkData.append(LastChunk.copy())
        if axis == 'x':
            if value == '-':
                xmin, ymin = -WinWidth, -WinHeight
                xmax, ymax = 0, 2*WinHeight
                spawnTree([xmax, ymax], [xmin, ymin])
            else:
                xmin, ymin = WinWidth, -WinHeight
                xmax, ymax = 2*WinWidth, 2*WinHeight
                spawnTree([xmax, ymax], [xmin, ymin])
        else:
            if value == '-':
                xmin, ymin = -WinWidth, -WinHeight
                xmax, ymax = 2*WinWidth, 0
                spawnTree([xmax, ymax], [xmin, ymin])
            else:
                xmin, ymin = -WinWidth, WinHeight
                xmax, ymax = 2*WinWidth, 2*WinHeight
                spawnTree([xmax, ymax], [xmin, ymin])



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
        if event.type == pygame.MOUSEBUTTONDOWN:
            Destroy(MeX, MeY)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        MeSpeed = 10
    else:
        MeSpeed = 5
    if keys[pygame.K_w] and Check(MeX, MeY, TreeData, 0, -MeSpeed):
        value, axis = '-', 'y'
        TextCoordinates = Transport(value, axis)
    if keys[pygame.K_d] and Check(MeX, MeY, TreeData, MeSpeed, 0):
        value, axis = '+', 'x'
        TextCoordinates = Transport(value, axis)
    if keys[pygame.K_s] and Check(MeX, MeY, TreeData, 0, MeSpeed):
        value, axis = '+', 'y'
        TextCoordinates = Transport(value, axis)
    if keys[pygame.K_a] and Check(MeX, MeY, TreeData, -MeSpeed, 0):
        value, axis = '-', 'x'
        TextCoordinates = Transport(value, axis)


