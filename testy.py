import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Guy:
  def __init__(self, x, y, color=(255,0,0)):
    self.x = x
    self.y = y
    self.rect = pygame.Rect(x, y, 10, 10)
    self.color = color
    self.vector = pygame.math.Vector2(-5, -1)

  def update(self, surf):
    pygame.draw.rect(surf, self.color, self.rect)


a = Guy(900, 100, (0, 150, 150))
b = Guy(700, 600)
# b.vector.rotate_ip(90)

while running:
  clock.tick(40)
  for e in pygame.event.get():
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        running = False

    if e.type == pygame.MOUSEBUTTONDOWN:
      a.x, a.y = e.pos[0], e.pos[1]
  
  b2a = pygame.math.Vector2(a.x-b.x, a.y-b.y)
  b2a.scale_to_length(50)
  # print("b2a", b2a)
  # print(b.vector)
  b.vector = b.vector.lerp(b2a, 0.05)
  b.vector.scale_to_length(50)
  # b.vector.update(b.x, b.y)
  # b2a.update(a.x, a.y)
  # print(b.vector)
  # angle = b.vector.angle_to(b2a)
  # print(angle/6)
  # b.vector.rotate_ip(angle)
  # print(b.vector.x)
  b.x += b.vector.x / 50
  b.y += b.vector.y / 50
  b.rect.x = b.x
  b.rect.y = b.y

  a.rect.x, a.rect.y = a.x, a.y

  # b.vector.update(b.x, b.y)
  screen.fill((70,70,70))
  a.update(screen)
  b.update(screen)
  pygame.display.update()