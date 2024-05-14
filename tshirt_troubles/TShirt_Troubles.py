import pygame
from helpers.player import Player
from helpers.minigame import *

pygame.init()
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
running_main = True
game_mode = "store"

WALK_SPEED = 5

player = Player(100, 100, 50, 50)

counter = pygame.Rect(500, 300, 580, 100)
cutting = pygame.Rect(900, 400, 80, 80)
OBSTACLES = [counter, cutting]

CUTTING_GAME = Minigame()

def move_player(keys, player, obstacles):
  last_position = (player.x, player.y)
  
  if keys[pygame.K_a]:
    player.x -= WALK_SPEED
    player.facing = "left"
  if keys[pygame.K_d]:
    player.x += WALK_SPEED
    player.facing = "right"
  
  player.rect.x = player.x

  if player.rect.collidelist(obstacles) != -1 or player.x > 1030 or player.x < 0:
    player.x = last_position[0]
    player.rect.x = player.x

  if keys[pygame.K_w]:
    player.y -= WALK_SPEED
    player.facing = "up"
  if keys[pygame.K_s]:
    player.y += WALK_SPEED
    player.facing = "down"
  
  player.rect.y = player.y

  if player.rect.collidelist(obstacles) != -1 or player.y > 870 or player.y < 0:
    player.y = last_position[1]
    player.rect.y = player.y

while running_main:
  clock.tick(60)
  screen.fill((90, 90, 90))
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      running_main = False
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        running_main = False
      if e.key == pygame.K_c:
        game_mode = "cut"
      if e.key == pygame.K_0:
        game_mode = "store"
  
  key_pressed = pygame.key.get_pressed()
  if game_mode == "store":
    move_player(key_pressed, player, OBSTACLES)
    if key_pressed[pygame.K_SPACE]:
      check = player.interact()
      pygame.draw.rect(screen, (0,255,0), check)
      if check.colliderect(cutting):
        game_mode = "cut"

    pygame.draw.rect(screen, (0, 0, 0), player.rect)
    

    # if key_pressed[]
    
    for object in OBSTACLES:
      pygame.draw.rect(screen, (255, 0, 0), object)
    pygame.draw.rect(screen, (0, 0, 255), cutting)
  
  elif game_mode == "cut":
    pygame.draw.rect(screen, CUTTING_GAME.background, CUTTING_GAME.rect)
  pygame.display.update()