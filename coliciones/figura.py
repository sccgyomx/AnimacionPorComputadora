import cmath
import math
import random

import pygame


class figura:
    COLOR = [255, 255, 255]
    ROJO = [255, 0, 0]
    dirX = 1
    dirY = 1

    def __init__(self, screen, x, y, tam, vel,acel):
        self.screen = screen
        self.x = x
        self.y = y
        self.tam = tam
        self.vel = vel
        self.acel = acel

    def movfig(self, figura):
        if figura == "circulo":
            pygame.draw.circle(self.screen, self.COLOR, [self.x, self.y], self.tam, 0)
            pygame.draw.circle(self.screen, self.ROJO,[self.x, self.y], 1, 0)
            #print("X : ", self.x, "Y:", self.y)
        if figura == "cuadrado":
            pygame.draw.rect(self.screen, self.COLOR, [self.x, self.y, self.x+10,self.y+10], 0)
            pygame.draw.circle(self.screen, self.ROJO, [self.x, self.y], 1, 0)
            #print("X : ", self.x, "Y:", self.y)
        if figura == "elipse":
            pygame.draw.ellipse(self.screen, self.COLOR, [self.x, self.y, self.x + 5, self.y + self.tam])
            pygame.draw.circle(self.screen, self.ROJO, [self.x, self.y], 1, 0)
            #print("X : ",self.x, "Y:", self.y)
        self.vel = self.vel*self.acel
        self.y = self.y + self.dirY*self.vel
        self.x = self.x + self.dirX*self.vel

        if self.x >= 800:
            self.dirX = -1
        if self.x <= 0:
            self.dirX = 1
        if self.y >= 600:
            self.dirY = -1
        if self.y <= 0:
            self.dirY = 1

    def detecCols(self, figura):
        distX = self.x - figura.x
        distY = self.y - figura.y
        distT = math.sqrt(math.pow(distX, 2)+math.pow(distY, 2))
        tamT = self.tam/2 + figura.tam/2
        if distT < tamT: # detecta colisión
            if distT != 0:
                print("Se detecto una colision ",tamT, "dist:",distT)
                self.COLOR =[random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)]

                # Rebote asignado (-X,-Y)
                #self.dirX*= -1
                self.dirY*= -1
                #figura.dirY*= -1
                figura.dirX*= -1
                return True
        else:
            return False
        pass
