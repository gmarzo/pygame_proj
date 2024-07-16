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
    self.vector = pygame.math.Vector2(0, 1)

  def update(self, surf):
    pygame.draw.rect(surf, self.color, self.rect)


a = Guy(900, 100, (0, 150, 150))
b = Guy(100, 600)

while running:
  clock.tick(40)
  for e in pygame.event.get():
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        running = False
  
  b2a = pygame.math.Vector2(a.x-b.x, a.y-b.y)
  b2a.normalize_ip()
  # print("b2a", b2a)
  print(b.vector)
  b.vector = b.vector.lerp(b2a, 0.5)
  print(b.vector)
  b.vector.normalize_ip()
  # print(b.vector)

  b.rect.x += b.vector.x
  b.rect.y += b.vector.y
  b.x += b.vector.x
  b.y += b.vector.y
  #b.vector.update(b.x, b.y)
  screen.fill((70,70,70))
  a.update(screen)
  b.update(screen)
  pygame.display.update()