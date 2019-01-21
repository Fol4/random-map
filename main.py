import pygame

'init'

pygame.init()
pygame.display.init()

'constant'

#delay
delay = 30

#runloop
GameRun = True

#window
WinWidth , WinHeight = 1280, 1024
window = pygame.display.set_mode((WinWidth, WinHeight))

#me
MeWidth , MeHeight = WinWidth//100, WinHeight//100
MeX , MeY = WinWidth//2, WinHeight//2
me = pygame.Surface((MeWidth, MeHeight))
me.fill((63,81,181))
MeSpeed = 5

#TEST
TestWidth , TestHeight = WinWidth//100, WinHeight//100
TestX , TestY = 300, 300
test = pygame.Surface((TestWidth , TestHeight))
test.fill((213,0,0))

# def drawMe():




'mainloop'

while GameRun:
    pygame.display.update()
    pygame.time.delay(delay)
    window.fill((46,125,50))
    window.blit(me, (MeX, MeY))
    window.blit(test, (TestX, TestY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRun = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        TestY += MeSpeed
    if keys[pygame.K_d]:
        TestX -= MeSpeed
    if keys[pygame.K_s]:
        TestY -= MeSpeed
    if keys[pygame.K_a]:
        TestX += MeSpeed



