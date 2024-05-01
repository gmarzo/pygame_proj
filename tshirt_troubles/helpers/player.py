import pygame

class Player():
  def __init__(self, x, y, height, width):
    self.x = x
    self.y = y
    self.rect = pygame.Rect(x, y, height, width)