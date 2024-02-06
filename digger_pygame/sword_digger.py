import os
import pygame

class Sprite(pygame.sprite.Sprite): 
    def __init__(self, height, width, images): 
        super().__init__() 
    
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

    def new_sword(self):
        # This function can be changed to pick a random instead of cycling
        self.img_index = (self.img_index + 1) % len(self.images)
        self.image = self.images[self.img_index]


pygame.init()    
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

running_images = [pygame.image.load("../sleepyboyJump/sleepyboy/"+x).convert() for x in os.listdir("../sleepyboyJump/sleepyboy")]
sword_images = [pygame.image.load("./swords/"+x).convert() for x in os.listdir("./swords")]

digger = Digger(400, 300, running_images)
sword = Sword(200, 400, sword_images)



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