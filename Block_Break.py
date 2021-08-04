#-*- coding: cp949 -*-
#-*- coding: utf-8 -*-


import sys
import math
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect

class Block:
    def __init__(self, col, rect, speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270

    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir))\
             * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))\
             * self.speed

    def draw(self):
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)
