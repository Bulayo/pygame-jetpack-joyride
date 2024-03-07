import pygame
import time
from entities import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/p1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft = (300, 570))
        self.roof_surf = pygame.image.load("assets/roof.png").convert_alpha()
        self.roof_rect = self.roof_surf.get_rect()
        self.floor_surf = pygame.image.load("assets/floor.png").convert_alpha()
        self.floor_rect = self.image.get_rect(topleft = (0, 576))
        self.fly_speed = 0
        self.is_flying = False
        self.gravity = 0
        self.gravity_delay = 0
        self.bullet_group = pygame.sprite.Group()
        self.bullet_delay = 0
        self.lazar_group = pygame.sprite.Group()


    def draw(self, win):
        win.blit(self.image, self.rect)
        self.bullet_group.draw(win)
        self.bullet_group.update()
        self.lazar_group.draw(win)
        self.lazar_group.update()


    def move(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE] or mouse[0]) and self.rect.top >= 64:
            self.is_flying = True
            self.fly_speed += 1
            if self.fly_speed >= 10:
                self.fly_speed = 10

            self.rect.y -= self.fly_speed
        
        else:
            self.is_flying = False
            self.fly_speed = 0


        self.update()


    def update(self):

        if self.rect.bottom >= 576:
            self.gravity = 0
            self.rect.bottom = self.floor_rect.top

        elif self.rect.top <= 64:
            self.rect.top = self.roof_rect.bottom + 1

        if self.is_flying:
            self.gravity = 0

        if self.is_flying and time.time() - self.bullet_delay >= 0.1:
            self.bullet = Bullet((self.rect.centerx - 20, self.rect.centery + 30))
            self.bullet_group.add(self.bullet)
            self.bullet_delay = time.time()
            

        elif not self.is_flying and time.time() - self.bullet_delay >= 0.12:
            self.gravity += 1
            if self.gravity >= 8:
                self.gravity = 8
            self.rect.y += self.gravity
            self.gravity_delay = time.time()

        self.lazar = Lazars()
        if len(self.lazar_group) <= 6:
            self.lazar_group.add(self.lazar)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, spawn):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = spawn

    def update(self):
        self.rect.y += 15

        if self.rect.bottom >= 576:
            self.kill()
