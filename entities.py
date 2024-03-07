import pygame
import random

class Lazars(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/zap2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (random.randint(160, 200), 58))
        self.image = pygame.transform.rotate(self.image, (random.randint(0, 360)))
        self.mask_image = pygame.mask.from_surface(self.image)
        x_pos = random.randint(1000, 4000)
        y_pos = random.randint(40, 600)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))


    def update(self):
        self.rect.x -= 5

        if self.rect.right <= 0:
            self.kill()

