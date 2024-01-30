import os
import pygame

class Sprite(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.image.get_rect() 
        self.state = {}


def handle_animation(player_sprite):
    global running_images
    global run_iter
    global idle
    global ySpeed
    new_img = idle
    keys = pygame.key.get_pressed()
    if player_sprite.state["grounded"]:
      if keys[pygame.K_d] or keys[pygame.K_a]:
        if player_sprite.state["anim"] == "idle":
            player_sprite.state["anim"] = "run"
            new_img = running_images[0]
        elif player_sprite.state["anim"] == "run":
            if run_iter == len(running_images):
                run_iter = 0
            new_img = running_images[run_iter]
            run_iter += 1
      
      else:
          run_iter = 0
          player_sprite.state["anim"] = "idle"
          new_img = idle
    elif player_sprite.state["grounded"] == False:
        if ySpeed < 0:
            player_sprite.state["anim"] = "fall"
            new_img = idle
        else:
            player_sprite.state["anim"] = "rise"
            new_img = idle
    
    player_sprite.image = new_img


def update_physics():
    global xSpeed
    global ySpeed
    global player
    global ground
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        xSpeed = 5
    elif keys[pygame.K_a]:
        xSpeed = -5
    else:
        xSpeed = 0
    if keys[pygame.K_SPACE] and player.state["grounded"]:
        #Jump physics
        ySpeed = -20
        player.state["grounded"] = False
        pass
    
    player.rect.x += xSpeed
    player.rect.y += ySpeed
    if not player.state["grounded"]:
      ySpeed += 1
      if pygame.sprite.collide_rect(player, ground):
          ySpeed = 0
          player.state["grounded"] = True
          while pygame.sprite.collide_rect(player, ground):
              player.rect.y -= 1
    

    

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

xSpeed = 0
ySpeed = 0


idle = pygame.image.load("idle.png").convert()
running_images = [pygame.image.load("./sleepyboy/"+x).convert() for x in os.listdir("./sleepyboy")]
print(idle, running_images)
run_iter = 0

player = Sprite((255, 255, 255), 100, 100)
player.image = idle
player.rect.x, player.rect.y = 100, 100
player.state = {"anim":"idle","grounded":True}

ground = Sprite((0, 255, 0), 50, 1280)
ground.rect.x, ground.rect.y = 0, 670


sprite_group = pygame.sprite.Group()

sprite_group.add(player)
sprite_group.add(ground)

while running:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            print("quit recieved")
            running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
    
    update_physics()
    handle_animation(player)


    screen.fill("purple")
    sprite_group.update()
    sprite_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()