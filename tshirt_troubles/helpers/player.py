import pygame

class Player():
  def __init__(self, x, y, height, width):
    self.x = x
    self.y = y
    self.rect = pygame.Rect(x, y, height, width)
    self.facing = "down"
  
  def interact(self):
    hitbox = pygame.Rect(self.x, self.y, 15, 15)
    match(self.facing):
      case "down":
        hitbox.x = self.rect.centerx
        hitbox.y = self.rect.centery + 20
      case "left":
        hitbox.x = self.rect.centerx - 20
        hitbox.y = self.rect.centery
      case "up":
        hitbox.x = self.rect.centerx
        hitbox.y = self.rect.centery - 20
      case "right":
        hitbox.x = self.rect.centerx + 20
        hitbox.y = self.rect.centery
    
    return hitbox