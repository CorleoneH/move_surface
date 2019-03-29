
import pygame, sys
from pygame.locals import *
from settings import Setting
from player import Player

pygame.init()

settings = Setting()        #create a setting instance
player = Player()       #create a player instance

SYSClock = pygame.time.Clock()

screen = pygame.display.set_mode(settings.screen_size)
pygame.display.set_caption('move_surface')

while True:
    screen.fill(settings.bg_color)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                sys.exit()
    player.update(settings.sur_speed)
    screen.blit(player.image, player.rect)
    pygame.display.update()
    SYSClock.tick(settings.fps)
