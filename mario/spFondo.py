import pygame, time, sys
from pygame.locals import *

fondo = (255, 255, 255)
altoX = 461
anchoY = 754
inc = 1
posiX = 0
posix = 0
posiY = 0

pX = 0
pY = 150
velocida=2

fps=60

reloj=pygame.time.Clock()

sp1 = pygame.image.load("./sprite_Fondo/tile000.png")
sp2 = pygame.image.load("./sprite_Fondo/tile001.png")
sp3 = pygame.image.load("./sprite_Fondo/tile002.png")
sp4 = pygame.image.load("./sprite_Fondo/tile003.png")
sp5 = pygame.image.load("./sprite_Fondo/tile004.png")
sp6 = pygame.image.load("./sprite_Fondo/tile005.png")
sp7 = pygame.image.load("./sprite_Fondo/tile006.png")
sp8 = pygame.image.load("./sprite_Fondo/tile007.png")
sp9 = pygame.image.load("./sprite_Fondo/tile008.png")
sp10 = pygame.image.load("./sprite_Fondo/tile009.png")

sp1 = pygame.transform.scale(sp1,[150,170])
sp2 = pygame.transform.scale(sp2,[150,170])
sp3 = pygame.transform.scale(sp3,[150,170])
sp4 = pygame.transform.scale(sp4,[150,170])
sp5 = pygame.transform.scale(sp5,[150,170])
sp6 = pygame.transform.scale(sp6,[150,170])
sp7 = pygame.transform.scale(sp3,[150,170])
sp8 = pygame.transform.scale(sp4,[150,170])
sp9 = pygame.transform.scale(sp5,[150,170])
sp10 = pygame.transform.scale(sp6,[150,170])
pantalla = pygame.display.set_mode((anchoY, altoX))
sprite = [
    sp1,
    sp2,
    sp3,
    sp4,
    sp5,
    sp6,
    sp7,
    sp8,
    sp9,
    sp10,
]

spFondo= pygame.image.load("interior.png").convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    cont = 0
    while (True):

        posiX_relativa= posiX % spFondo.get_rect().width
        pantalla.blit(spFondo,(posiX_relativa-spFondo.get_rect().width, 0))
        
        if posiX_relativa<754:
            pantalla.blit(spFondo,(posiX_relativa, 0))
        
        if cont==9:
            cont=0

        pantalla.blit(sprite[cont],[pX, pY])
        posiX-=7
        cont+=1
        pygame.display.update()
        time.sleep(.1)