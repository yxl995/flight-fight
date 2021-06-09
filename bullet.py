import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position[0] - 13, position[1]
        self.speed = 8
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position[0] - 13, position[1]
        self.active = True
