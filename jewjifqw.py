import pygame
import random
width = 500
height = 400
speed = 5
font_size = 72
pygame.init()
screen = pygame.display.set((500,400))
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super.__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("Orange"))
        pygame.draw.rect(self.image, color, pygame.Rect(0,0,width, height))
        self.rect = self.image.get_rect()
    def move(self,xchange, ychange):
        self.rect.rect.x = max(min(self.xchange,width-self.rect,width))
        self.rect.rect.y = max(min(self.ychange,width-self.rect,width))
        
        