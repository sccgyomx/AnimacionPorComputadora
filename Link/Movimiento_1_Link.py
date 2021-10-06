import pygame
import sys
import time
from pygame.locals import *

pygame.init()
fondo = (255, 255, 255)
altoY = 600
anchoX = 800
posIx = 30
posIy = 100
posILx = 720
posILy = 500
posicion=[30,100]
splink = []
splinkE = []
Font=pygame.font.SysFont('timesnewroman',  30)
black=(0, 0, 0)

pantalla = pygame.display.set_mode((anchoX, altoY))
for i in range(12):
    aux = int.__str__(i)
    splink.append(pygame.image.load("link"+aux+".png"))
    for spl in splink:
        splinkE.append(pygame.transform.scale(spl,(52,75)))
sprPr = pygame.transform.scale2x(pygame.image.load("linkP.png"))
frame_act = 0
frames = 11
fr_ancho = 48
fr_alto = 70
cont = 0


spriteL = pygame.sprite.Sprite
spriteL.image = sprPr
spriteL.rect = spriteL.image.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for spl in splinkE:
        n_rec = pygame.Rect((frame_act * fr_ancho ,0,fr_ancho-1,fr_alto))
        pantalla.fill(fondo)
        # altoY = 600
        # anchoX = 800
        # posIx = 30
        # posIy = 100

        if (posicion[0] < 720 and posicion[1] == 100):
          pantalla.blit(spriteL.image.subsurface(n_rec),(posIx + cont, posIy))
          posicion[0]=posIx + cont
          if(posicion[0]==720):
            cont=0

        if (posicion[0] == 720 and posicion[1] <500):
          pantalla.blit(spriteL.image.subsurface(n_rec),(posILx , posIy+ cont))
          posicion[1]=posIy+ cont
          if(posicion[1]==500):
            cont=0
        if (posicion[0] > 30 and posicion[1] == 500):
          posicion[0]=posILx - cont
          pantalla.blit(spriteL.image.subsurface(n_rec),(posILx - cont, posILy))
          if(posicion[0]==30):
            cont=0

        if (posicion[0] == 30 and posicion[1] >100):
          posicion[1]=posILy- cont
          pantalla.blit(spriteL.image.subsurface(n_rec),(posIx , posILy- cont))
          if(posicion[1]==100):
            cont=0

        pantalla.blit( Font.render(("x: {}, y: {}").format(posicion[0],posicion[1]),False,black)  , (30, 30))

        if (frame_act>frames-1):
          frame_act=0
        else:
          frame_act += 1


        cont+=1
        pygame.display.update()
        time.sleep(.05)
