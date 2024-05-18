import pygame

pygame.init()

screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
running = True

player_img = pygame.transform.scale(pygame.image.load("rip.png"), (100, 66))
player_hitbox = player_img.get_rect()
p_x = 400
p_y = 50
p_xspeed = 0
p_yspeed = 0
p_isGrounded = False
p_isFastFalling = False
p_stats = {"MAX_GROUND_SPEED": 10, "MAX_FALL_SPEED": 12, "GRAVITY": 2, "MIDAIR_JUMPS": 1}
p_midairJumps = p_stats["MIDAIR_JUMPS"]

pipe_fall = pygame.mixer.Sound("pipe.mp3")
#pygame.mixer.music.load("copyright_infringement.mp3")

stage = pygame.Rect(240, 600, 600, 150)

stage_ground = (241, 600, 839, 600)
stage_left_wall = (240, 600, 240, 750)
stage_right_wall = (840, 600, 840, 750)

# Name given to the death zones that kill the player
blast_zone_top = 0
blast_zone_bot = 920
blast_zone_right = 1080
blast_zone_left = 0

left_test = pygame.Rect(240, 600, 10, 140)
right_test = pygame.Rect(830, 600, 10, 140)
top_test = pygame.Rect(241, 600, 598, 10)

#pygame.mixer.music.play()

while running:

  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      print("QUIT)")
      running = False
    
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        pygame.quit()

  keys_pressed = pygame.key.get_pressed()

  # Calculate horizontal player movement per frame
  if keys_pressed[pygame.K_d]:
    p_xspeed = min(p_xspeed + 1, p_stats["MAX_GROUND_SPEED"])
  elif keys_pressed[pygame.K_a]:
    p_xspeed = max(p_xspeed - 1, -p_stats["MAX_GROUND_SPEED"])
  else:
    p_xspeed *= 0.8

  # Calculate vertical player movement per frame
  if keys_pressed[pygame.K_w] and p_isGrounded:
    p_yspeed = -30
  elif not p_isGrounded and not p_isFastFalling:
    if keys_pressed[pygame.K_w]:
      p_yspeed = min(p_yspeed + p_stats["GRAVITY"], p_stats["MAX_FALL_SPEED"])
    elif not keys_pressed[pygame.K_w]:
      if p_yspeed < -1:
        p_yspeed *= 0.7
      else:
        p_yspeed = min(p_yspeed + p_stats["GRAVITY"], p_stats["MAX_FALL_SPEED"])
    # Use a midair jump
    if keys_pressed[pygame.K_w] and p_yspeed > 0 and p_midairJumps > 0:
      p_yspeed = -30
      p_midairJumps -= 1
      p_isFastFalling = False

    # Fast fall by pressing down in mid-air
    if keys_pressed[pygame.K_s] and not p_isFastFalling and p_yspeed > 0:
      p_yspeed = p_stats["MAX_FALL_SPEED"] * 2
      p_isFastFalling = True  
  elif not p_isGrounded and p_isFastFalling:
    if keys_pressed[pygame.K_w] and p_yspeed > 0 and p_midairJumps > 0:
      p_yspeed = -30
      p_midairJumps -= 1
      p_isFastFalling = False
  elif p_isGrounded:
      p_yspeed = 0
      p_isFastFalling = False
  
  
  p_x += p_xspeed
  p_y += p_yspeed

  player_hitbox.x = p_x
  player_hitbox.y = p_y

  
  # Check for ground collision
  if player_hitbox.clipline(stage_ground):
    p_isGrounded = True
    p_isFastFalling = False
    p_midairJumps = p_stats["MIDAIR_JUMPS"]
    while player_hitbox.bottom > stage_ground[1] + 1:
      p_y -= 1
      player_hitbox.y = p_y
  else:
    p_isGrounded = False

  # Check against walls
  if player_hitbox.clipline(stage_left_wall) and not p_isGrounded:
    p_xspeed = 0
    while player_hitbox.right > stage_left_wall[0]:
      p_x -= 1
      player_hitbox.x = p_x
  if player_hitbox.clipline(stage_right_wall) and not p_isGrounded:
    p_xspeed = 0
    while player_hitbox.left < stage_right_wall[0]:
      p_x += 1
      player_hitbox.x = p_x


  # "Respawn" player on death
  if player_hitbox.top > blast_zone_bot or player_hitbox.left > blast_zone_right or player_hitbox.bottom < blast_zone_top or player_hitbox.right < blast_zone_left:
    p_x = 400
    p_y = 300
    p_midairJumps = p_stats["MIDAIR_JUMPS"]
    p_isFastFalling = False
    pygame.mixer.Sound.play(pipe_fall)

  # print(p_yspeed, p_isGrounded, p_isFastFalling)
  screen.fill((45, 45, 45))
  pygame.draw.rect(screen, (89, 45, 5), stage)

  # Debug rects to approximate walls and floor
  # pygame.draw.rect(screen, (255, 0, 0), left_test)
  # pygame.draw.rect(screen, (255, 0, 0), right_test)
  # pygame.draw.rect(screen, (0, 0, 255), top_test)

  screen.blit(player_img, (p_x, p_y))

  # Debug check for when grounded
  # if p_isGrounded:
  #   pygame.draw.rect(screen, (255, 0, 0), player_hitbox)
  clock.tick(60)

  pygame.display.update()