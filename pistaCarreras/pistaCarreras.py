import pygame
import sys
import time
from pygame.locals import *
import random

pygame.init()
altoY = 461
anchoX = 754
AltoAncho=30
velocidad=1
aceleracionJugador1=1
aceleracionJugador2=1
bandera1=0
fps=60
reloj=pygame.time.Clock()

Font=pygame.font.SysFont('timesnewroman',  20)
color=(0, 0, 0) ##15ab92

pantalla = pygame.display.set_mode((anchoX, altoY))
fondo= pygame.image.load("Pista.png").convert()
jugador1=pygame.transform.scale((pygame.image.load("poop.png").convert()), (AltoAncho, AltoAncho))
jugador2=pygame.transform.scale((pygame.image.load("angry.png").convert()), (AltoAncho, AltoAncho))
posicionJugador1=[430,40]
posicionJugador2=[415,60]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # logica de aceleracion para jugador1
    if(posicionJugador1[0]==480 and posicionJugador1[1]==250):
        aceleracionJugador1=random.randint(1, 3)
    if(posicionJugador1[0]==120 and posicionJugador1[1]>=390):
        aceleracionJugador1=random.randint(1, 3)
    if(posicionJugador1[0]==180 and posicionJugador1[1]<40):
        aceleracionJugador1=random.randint(1, 3)

    # logica de movimiento del jugador1
    if(posicionJugador1[0]<630 and posicionJugador1[1]<=40):
        posicionJugador1[0]=posicionJugador1[0]+(velocidad*aceleracionJugador1)
        bandera1=0
    if(posicionJugador1[0]>=630 and posicionJugador1[1]<250):
        posicionJugador1[1]=posicionJugador1[1]+(velocidad*aceleracionJugador1)
    if(posicionJugador1[0]>390 and posicionJugador1[1]>=250):
        posicionJugador1[0]=posicionJugador1[0]-(velocidad*aceleracionJugador1)
    if(posicionJugador1[0]==390 and posicionJugador1[1]>249):
        if(posicionJugador1[1]<390):
            posicionJugador1[1]=posicionJugador1[1]+(velocidad*aceleracionJugador1)
    if(posicionJugador1[0]>60 and posicionJugador1[1]>=390):
        posicionJugador1[0]=posicionJugador1[0]-(velocidad*aceleracionJugador1)
    if(posicionJugador1[0]<=60 and posicionJugador1[1]>40):
        posicionJugador1[1]=posicionJugador1[1]-(velocidad*aceleracionJugador1)

    # logica de aceleracion para jugador2
    if(posicionJugador2[0]==480 and posicionJugador2[1]==250):
        aceleracionJugador2=random.randint(1, 3)
    if(posicionJugador2[0]==120 and posicionJugador2[1]>=390):
        aceleracionJugador2=random.randint(1, 3)
    if(posicionJugador2[0]==180 and posicionJugador2[1]<40):
        aceleracionJugador2=random.randint(1, 3)

    # logica de movimiento del jugador2
    if(posicionJugador2[0]<630 and (posicionJugador2[1]<=40 or posicionJugador2[1]<=60)):
        posicionJugador2[0]=posicionJugador2[0]+(velocidad*aceleracionJugador2)
    if(posicionJugador2[0]>=630 and posicionJugador2[1]<250):
        posicionJugador2[1]=posicionJugador2[1]+(velocidad*aceleracionJugador2)
    if(posicionJugador2[0]>390 and posicionJugador2[1]>=250):
        posicionJugador2[0]=posicionJugador2[0]-(velocidad*aceleracionJugador2)
    if(posicionJugador2[0]==390 and posicionJugador2[1]>249):
        if(posicionJugador2[1]<390):
            posicionJugador2[1]=posicionJugador2[1]+(velocidad*aceleracionJugador2)
    if(posicionJugador2[0]>60 and posicionJugador2[1]>=390):
        posicionJugador2[0]=posicionJugador2[0]-(velocidad*aceleracionJugador2)
    if(posicionJugador2[0]<=60 and posicionJugador2[1]>40):
        posicionJugador2[1]=posicionJugador2[1]-(velocidad*aceleracionJugador2)

    pantalla.blit(fondo,(0,0))
    pantalla.blit(jugador1,(posicionJugador1[0],posicionJugador1[1]))
    pantalla.blit(jugador2,(posicionJugador2[0],posicionJugador2[1]))
    pantalla.blit( Font.render(("Poop => x: {}, y: {}, Aceleracion:{}      Angry => x: {}, y: {}, Aceleracion:{}")
    .format(posicionJugador1[0],posicionJugador1[1],aceleracionJugador1,posicionJugador2[0],posicionJugador2[1],
    aceleracionJugador2),False,color)  , (10, 10))

    reloj.tick_busy_loop(30)
    pygame.display.set_caption("fps: " + str(reloj.get_fps()))
    pygame.display.update()