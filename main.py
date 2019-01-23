import pygame

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
WinWidth , WinHeight = 1280, 1024
window = pygame.display.set_mode((WinWidth, WinHeight))

# ME
MeWidth , MeHeight = WinWidth//100, WinHeight//100
MeX , MeY = WinWidth//2, WinHeight//2
x , y = MeX, MeY
me = pygame.Surface((MeWidth, MeHeight))
me.fill((63,81,181))
MeSpeed = 5

# TEXT
FontXY = pygame.font.Font(None , 22)
FontX, FontY = 0, 0
TextCoordinates = FontXY.render('x : ' + str(MeX) + ' , y : ' + str(MeY) , True , (0,0,0))


# TEST
TestWidth , TestHeight = WinWidth//100, WinHeight//100
TestX , TestY = 300, 300
test = pygame.Surface((TestWidth , TestHeight))
test.fill((213,0,0))
test2 = pygame.Surface((TestWidth, TestHeight))
test2.fill((221,44,0))
Test2X , Test2Y = -TestX, -TestY

# def drawTree():


'MAINLOOP'

while GameRun:
    pygame.display.update()
    pygame.time.delay(delay)
    window.fill((46,125,50))
    window.blit(me, (MeX, MeY))
    window.blit(test, (TestX, TestY))
    window.blit(TextCoordinates , (FontX, FontY))
    window.blit(test2 , (Test2X, Test2Y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRun = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y += MeSpeed
        TextCoordinates = FontXY.render('x : ' + str(x) + ' , y : ' + str(y) , True , (0,0,0))
        Test2Y += MeSpeed
        TestY += MeSpeed
    if keys[pygame.K_d]:
        x -= MeSpeed
        TextCoordinates = FontXY.render('x : ' + str(x) + ' , y : ' + str(y), True, (0, 0, 0))
        Test2X -= MeSpeed
        TestX -= MeSpeed
    if keys[pygame.K_s]:
        y -= MeSpeed
        TextCoordinates = FontXY.render('x : ' + str(x) + ' , y : ' + str(y), True, (0, 0, 0))
        Test2Y -= MeSpeed
        TestY -= MeSpeed
    if keys[pygame.K_a]:
        x += MeSpeed
        TextCoordinates = FontXY.render('x : ' + str(x) + ' , y : ' + str(y), True, (0, 0, 0))
        Test2X += MeSpeed
        TestX += MeSpeed



