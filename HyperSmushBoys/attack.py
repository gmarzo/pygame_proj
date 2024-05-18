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
  def __init__(self, hitboxes={}, images={}):
    self.hitboxes = hitboxes
    self.images = images
    self.current_frame = 0
    self.dt = 0

  def update(self, dt):
    self.dt += dt
    

  

