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
        hitbox.centerx = self.rect.centerx
        hitbox.centery = self.rect.centery + 50
      case "left":
        hitbox.centerx = self.rect.centerx - 50
        hitbox.centery = self.rect.centery
      case "up":
        hitbox.centerx = self.rect.centerx
        hitbox.centery = self.rect.centery - 50
      case "right":
        hitbox.centerx = self.rect.centerx + 50
        hitbox.centery = self.rect.centery
    
    return hitbox