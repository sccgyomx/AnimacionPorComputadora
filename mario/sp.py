import pygame, time, sys
from pygame.locals import *
fondo = (255, 255, 255)
altoX = 200
anchoY = 200
inc = 1
posiX = 0
posiY = 0
sp1 = pygame.image.load("./MySprite/tile000.png")
sp2 = pygame.image.load("./MySprite/tile001.png")
sp3 = pygame.image.load("./MySprite/tile002.png")
sp4 = pygame.image.load("./MySprite/tile003.png")
sp5 = pygame.image.load("./MySprite/tile004.png")
sp6 = pygame.image.load("./MySprite/tile005.png")

sp1 = pygame.transform.scale(sp1,[150,170])
sp2 = pygame.transform.scale(sp2,[150,170])
sp3 = pygame.transform.scale(sp3,[150,170])
sp4 = pygame.transform.scale(sp4,[150,170])
sp5 = pygame.transform.scale(sp5,[150,170])
sp6 = pygame.transform.scale(sp6,[150,170])
pantalla = pygame.display.set_mode((anchoY, altoX))
sprite = [
    sp1,
    sp2,
    sp3,
    sp4,
    sp5,
    sp6
]
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    cont = 0
    while (cont < 6):
        pantalla.fill(fondo)
        pantalla.blit(sprite[cont],[posiX, posiY])
        cont+=1
        pygame.display.update()
        time.sleep(.3)