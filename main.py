import pygame
from player import *

def bg_movement():

    bg1_rect.x -= 5
    bg2_rect.x -=5

    if bg1_rect.right <= 0:
        bg1_rect.left = 1000

    elif bg2_rect.right <= 0:
        bg2_rect.left = 1000

pygame.init()
pygame.mixer.init()

RES = WIDTH, HEIGHT = 1000, 640
WIN = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load("assets/background.png").convert_alpha()
background = pygame.transform.scale(background, (1000, 640))
bg1_rect = background.get_rect()
bg2_rect = background.get_rect(topleft = (1000, 0))

player = Player()

song = pygame.mixer.music.load("assets/theme_song.mp3")
pygame.mixer.music.play(loops= 100)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    WIN.blit(background, bg1_rect)
    WIN.blit(background, bg2_rect)
    bg_movement()
    player.draw(WIN)
    player.move()

    pygame.display.flip()
    clock.tick(FPS)
    WIN.fill((50, 50, 50))

pygame.quit()