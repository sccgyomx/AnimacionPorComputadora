from figura import *
import time
import pygame
import random

FONDO = [0,0,0]

pygame.init()

ventana = pygame.display.set_mode([800,600])
f1 = figura(ventana, random.randrange(10, 800),random.randrange(10,600),20,1,1)
f3 = figura(ventana, random.randrange(10, 800),random.randrange(10,600),20,1,1)
f4 = figura(ventana, random.randrange(10, 800),random.randrange(10,600),20,1,1)
f2 = figura(ventana,10,200,20,1,1)
ventA = True
figs = []
figs.append(f1)
figs.append(f2)
figs.append(f3)
figs.append(f4)
while ventA:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventA = False
    ventana.fill(FONDO)

    for fig in figs:
        fig.movfig("circulo")
        i = 0
        tamLis = figs.__len__()
        while(i < tamLis):
            if fig.detecCols(figs[i]):
                print("Indice Detecta: ",figs.index(fig,0,tamLis),"Indice Dectectado",i)
                figs.pop(i)
                tamLis = figs.__len__()
            i+= 1
    #f1.movfig("circulo")
    #f2.movfig("circulo")
    pygame.display.update()
    #time.sleep(.5)
pygame.quit()