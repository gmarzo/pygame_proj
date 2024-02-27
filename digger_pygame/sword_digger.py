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
        self.image = self.images[self.img_index]

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
            self.image = self.images[self.img_index]
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

    def new_sword(self):
        # This function can be changed to pick a random instead of cycling
        gacha_val = random.random()
        print(gacha_val)
        new_sword_img = None
        if gacha_val < 0.6:
          new_sword_img = self.swords["common"][random.randint(0, len(self.swords["common"])-1)]
        elif gacha_val < 0.9:
          new_sword_img = self.swords["rare"][random.randint(0,len(self.swords["rare"])-1)]
        else:
          new_sword_img = self.swords["ultra_rare"][random.randint(0,len(self.swords["ultra_rare"])-1)]

        # self.img_index = (self.img_index + 1) % len(self.images)
        scale_img = pygame.transform.scale(new_sword_img, (self.height, self.width))
        self.image = scale_img

    


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

running_images = [pygame.image.load("../sleepyboyJump/sleepyboy/"+x).convert() for x in os.listdir("../sleepyboyJump/sleepyboy")]
sword_images = [pygame.image.load("./swords/"+x).convert() for x in os.listdir("./swords")]

digger = Digger(400, 300, running_images)
sword = Sword(200, 200, sword_images)



all_sprites = pygame.sprite.Group()
all_sprites.add(digger)
all_sprites.add(sword)


while running:

    dt = clock.tick(60)/1000

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            print("quit recieved")
            running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
    if keys_pressed[pygame.K_SPACE]:
        if not digger.digging:
            digger.digging = True
            sword.new_sword()
    

    screen.fill((115,115,115))
    all_sprites.draw(screen)
    all_sprites.update(dt)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()