import pygame
import sys
import time
from pygame.locals import *

pygame.init()
fondo = (255, 255, 255)
altoY = 600
anchoX = 800

Font=pygame.font.SysFont('timesnewroman',  30)
pantalla = pygame.display.set_mode((anchoX, altoY))