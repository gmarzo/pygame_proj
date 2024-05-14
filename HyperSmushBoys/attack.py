import pygame

class Hitbox():
  def __init__(self, size, damage, knockback=0, direction=0, offset=(0,0)):
    self.size = size
    self.damage = damage
    self.knockback = knockback
    self.direction = direction
    self.offset = offset
    self.active = False

class Attack():
  def __init__(self, hitboxes=[], active_frames=0, images=[]):
    self.hitboxes = hitboxes
    self.active_frames = active_frames
    self.images = images
    self.dt = 0

  

