import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/小敌人.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load('images/小敌人-爆1.png').convert_alpha(), \
            pygame.image.load('images/小敌人-爆2.png').convert_alpha(), \
            pygame.image.load('images/小敌人-爆3.png').convert_alpha(), \
            pygame.image.load('images/小敌人-爆4.png').convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.level = 0
        self.speed = randint(1, 2 + self.level)
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

class MidEnemy(pygame.sprite.Sprite):

    energy = 6
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/中敌人.png').convert_alpha()
        self.image_hit = pygame.image.load('images/中敌人-击中.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load('images/中敌人-爆1.png').convert_alpha(), \
            pygame.image.load('images/中敌人-爆2.png').convert_alpha(), \
            pygame.image.load('images/中敌人-爆3.png').convert_alpha(), \
            pygame.image.load('images/中敌人-爆4.png').convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.level = 0
        self.speed = randint(1, 1 + self.level)
        self.active = True
        self.hit = False
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)
        self.energy = MidEnemy.energy

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.hit = False
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)
        self.energy = MidEnemy.energy
        
class BigEnemy(pygame.sprite.Sprite):

    energy = 11
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load('images/大敌人-1.png').convert_alpha()
        self.image2 = pygame.image.load('images/大敌人-2.png').convert_alpha()
        self.image_hit = pygame.image.load('images/大敌人-击中.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load('images/大敌人-爆1.png').convert_alpha(), \
            pygame.image.load('images/大敌人-爆2.png').convert_alpha(), \
            pygame.image.load('images/大敌人-爆3.png').convert_alpha(), \
            pygame.image.load('images/大敌人-爆4.png').convert_alpha(), \
            pygame.image.load('images/大敌人-爆5.png').convert_alpha(), \
            pygame.image.load('images/大敌人-爆6.png').convert_alpha()])
        self.rect = self.image2.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.level = 0
        self.speed = randint(1, 1 + self.level)
        self.active = True
        self.hit = False
        self.mask = pygame.mask.from_surface(self.image1)
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, -self.height)
        self.energy = BigEnemy.energy

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.hit = False
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, -self.height)
        self.energy = BigEnemy.energy
