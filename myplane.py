import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load('images/me-1.png')
        self.image2 = pygame.image.load('images/me-2.png')
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load('images/me-爆1.png').convert_alpha(), \
            pygame.image.load('images/me-爆2.png').convert_alpha(), \
            pygame.image.load('images/me-爆3.png').convert_alpha(), \
            pygame.image.load('images/me-爆4.png').convert_alpha()])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.speed = 5
        self.time = 800
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        if self.rect.top > 7:
            self.rect.top -= self.speed
        else:
            pass

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.bottom += self.speed
        else:
            pass

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            pass

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            pass
