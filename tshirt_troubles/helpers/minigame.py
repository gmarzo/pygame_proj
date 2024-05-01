import pygame
class Minigame():
  def __init__(self, screen_size=(700, 600), background=(40,40,40)):
    self.screen_size = screen_size
    self.background = background
    self.rect = pygame.Rect(200, 80, self.screen_size[0], self.screen_size[1])

