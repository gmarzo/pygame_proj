import os
import pygame
import random

class Sprite(pygame.sprite.Sprite): 
    def __init__(self, height, width, images): 
        super().__init__() 

        self.height = height
        self.width = width
    
        self.rect = pygame.Rect((0, 0), (height, width))

        self.images = images
        self.img_index = 0
        self.image = pygame.transform.scale(self.images[self.img_index], (self.height, self.width))

        self.animation_time = 0.06
        self.current_time = 0

        self.animation_frames = len(self.images)
        self.current_frame = 0

class Digger(Sprite):
    
    def __init__(self, height, width, images):
        super().__init__(height, width, images)
        self.digging = False
        self.rect.x, self.rect.y = 500, 300
    
    def update_frame(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.img_index = (self.img_index + 1)
            if self.img_index >= len(self.images):
                self.img_index = 0
                self.digging = False
            self.image = pygame.transform.scale(self.images[self.img_index], (self.height, self.width))
            self.current_time = 0

    def digging_time(self, dt):
        if self.digging:
            self.update_frame(dt)
    
    def update(self, dt):
        self.digging_time(dt)

class Sword(Sprite):
    
    def __init__(self, height, width, images):
        super().__init__(height, width, images)
        self.rect.x, self.rect.y = 800, 0

        self.swords = {"common": images[0:3],
                       "rare": images[3:5],
                       "ultra_rare": images[5:7]}

    def new_sword(self, value):
        gacha_val = value
        return_sword = 0
        print(gacha_val)
        new_sword_img = None
        if gacha_val < 0.6:
          return_rand = random.randint(0, len(self.swords["common"])-1)
          new_sword_img = self.swords["common"][return_rand]
        elif gacha_val < 0.9:
          return_sword += 3
          return_rand = random.randint(0,len(self.swords["rare"])-1)
          new_sword_img = self.swords["rare"][return_rand]
        else:
          return_sword += 5
          return_rand = random.randint(0,len(self.swords["ultra_rare"])-1)
          new_sword_img = self.swords["ultra_rare"][return_rand]

        # self.img_index = (self.img_index + 1) % len(self.images)
        scale_img = pygame.transform.scale(new_sword_img, (self.height, self.width))
        self.image = scale_img
        return return_sword + return_rand
    
class InventorySlot(Sprite):
    
    def __init__(self, height, width, images):
        super().__init__(height, width, images)
        self.revealed = False
        self.sword_img = pygame.transform.scale(images[0], (self.height, self.width))
        self.hidden_img = pygame.Surface((self.height, self.width))
        self.hidden_img.fill((0,0,0))

        print(self.hidden_img)
        self.image = self.hidden_img
    
    def reveal(self):
        self.revealed = True
        self.image = self.sword_img


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

running_images = [pygame.image.load("../sleepyboyJump/sleepyboy/"+x).convert() for x in os.listdir("../sleepyboyJump/sleepyboy")]
sword_images = [pygame.image.load("./swords/"+x).convert() for x in os.listdir("./swords")]
backpack_images = [pygame.image.load("backpack.png").convert()]

inventory_open = False

digger = Digger(500, 300, running_images)
sword = Sword(200, 200, sword_images)
backpack = Sprite(200, 200, backpack_images)

inventory = []

for i in range(len(sword_images)):
  inv_slot = InventorySlot(50, 50, [sword_images[i]])
  inv_slot.rect.x = 210 + 60*i
  inventory.append(inv_slot)

all_sprites = pygame.sprite.Group()
all_sprites.add(digger)
all_sprites.add(sword)
all_sprites.add(backpack)

while running:

    dt = clock.tick(60)/1000

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            print("quit recieved")
            running = False
      if event.type == pygame.MOUSEBUTTONUP:
          if backpack.rect.collidepoint(event.pos):
              inventory_open = not inventory_open
              if inventory_open:
                  for x in inventory:
                      all_sprites.add(x)
              else:
                  for x in inventory:
                      all_sprites.remove(x)


    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
    if keys_pressed[pygame.K_SPACE]:
        if not digger.digging:
            rand_val = random.random()
            digger.digging = True
            inventory[sword.new_sword(rand_val)].reveal()
    

    screen.fill((115,115,115))

    if inventory_open:
        dt = 0

    all_sprites.draw(screen)
    all_sprites.update(dt)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()