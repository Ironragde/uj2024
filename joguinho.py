# Example file showing a circle moving on screen
import pygame
import math
import random
# pygame setup

pygame.init()+
screen = pygame.display.set_mode((1800, 1000))
clock = pygame.time.Clock()
pygame.mouse.set_pos(screen.get_width() / 2, 0)
running = True
mouse_pos=pygame.mouse.get_pos()
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

this_tick = 0
last_tick = 0

while running:
    
    this_tick = pygame.time.get_ticks() % 3000
    mouse = True
    player = True
    mouse_pos=pygame.mouse.get_pos()
    dist_mp = mouse_pos - player_pos
    dist_mp_x = dist_mp[0]
    dist_mp_y = dist_mp[1]
    hip_mp = math.sqrt((dist_mp_y**2)+(dist_mp_x**2))
    ang_rad=math.asin(dist_mp_y/hip_mp)
    ang= int((ang_rad*180)/3.1415)
    rec = pygame.Vector2(player_pos.x, player_pos.y - 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    

    screen.fill("gray")
    player_pos_x = player_pos[0]
    player_pos_y = player_pos[1] 
    pygame.draw.circle(screen, "red", player_pos, 30)
    dir = pygame.math.Vector3(1,1,0)
  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        
        
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
  
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    def enemies():
        spawn_pos = pygame.Vector2(400,30)
        pygame.draw.circle(screen, "black", spawn_pos, 30)
    while player == True and this_tick<last_tick:
        enemies()
    last_tick = this_tick       

    
   
pygame.quit()