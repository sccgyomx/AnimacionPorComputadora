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
posILx = 730
posILy = 500
splink = []
splinkE = []
pantalla = pygame.display.set_mode((anchoX, altoY))
for i in range(12):
    aux = int.__str__(i)
    #print("link"+aux+".png", aux)
    #Se cargan las 11 imagenes del sprite en la lista splink
    splink.append(pygame.image.load("link"+aux+".png"))
    #se reescalan las imágenes
    for spl in splink:
        splinkE.append(pygame.transform.scale(spl,(52,75)))
    #print(splink)
sprPr = pygame.transform.scale2x(pygame.image.load("linkP.png"))
#sprPr=pygame.image.load("linkP.png")
#Se define la cantidad de frames y el tamaño de cada uno
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
        pantalla.blit(spriteL.image.subsurface(n_rec),(posIx + cont, posIy))
        pantalla.blit(spriteL.image.subsurface(n_rec),(posIx , posIy+ cont))
        pantalla.blit(spriteL.image.subsurface(n_rec),(posILx - cont, posILy))
        pantalla.blit(spriteL.image.subsurface(n_rec),(posILx , posILy- cont))
        
        
        print("frame: ",frame_act, "posX: ",frame_act * fr_ancho)

        if (frame_act>frames-1):
          frame_act=0
        else:
          frame_act += 1


        cont+=1
        # pantalla.blit(sprPr,(10,500))
        pygame.display.update()
        time.sleep(.05)
