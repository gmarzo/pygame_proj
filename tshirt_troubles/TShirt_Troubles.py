import pygame
import sys
from helpers.player import Player

pygame.init()
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
running_main = True

player = Player(100, 100, 50, 50)

while running_main:
  clock.tick(60)
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      running_main = False
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        pygame.quit()
  
  screen.fill((90, 90, 90))
  pygame.draw.rect(screen, (0, 0, 0), player.rect)
  pygame.display.update()