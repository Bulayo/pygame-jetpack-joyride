import pygame
import random
import time

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


class Indicator(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/danger.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (960, 0))
        self.can_move = True
        self.stop_moving = 0
        self.delay = 0
        self.rocket = False

    def update(self, ypos):

        if time.time() - self.stop_moving >= 2:
            self.can_move = False

            if time.time() - self.delay >= 4:
                self.stop_moving = time.time()
                self.delay = time.time()
                self.can_move = True
                self.rocket = True

        if self.can_move:
            self.rect.y = ypos

class Rocket(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/rocket.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (1000, 0))

    def update(self, ypos):
        
        self.rect.y = ypos
        self.rect.x -= 10

        if self.rect.right <= 0:
            self.kill()

