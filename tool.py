import pygame
from random import *

class Bomb(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/补给-炸弹.png')
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)

class SuperBullet(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/补给-双弹药.png')
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)
