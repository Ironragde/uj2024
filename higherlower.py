
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1800, 1000))
clock = pygame.time.Clock()
running = True
dt = 0
nivel1 = True
nivel2 = False
nivel3 = False
enemies = []
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
level1_enemies = []
inim1 = pygame.Rect(400, 200, 40,40)
inim2 = pygame.Rect(500, 760, 40,40)
inim3 = pygame.Rect(600, 200, 40,40)
inim4 = pygame.Rect(700, 760, 40,40)
inim5 = pygame.Rect(800, 200, 40,40)
inim6 = pygame.Rect(900, 760, 40,40)
inim7 = pygame.Rect(1000, 200, 40,40)
inim8 = pygame.Rect(1100, 760, 40,40)
inim9 = pygame.Rect(1200, 200, 40,40)
inim10 = pygame.Rect(1300, 760, 40,40)
inim11 = pygame.Rect(1400, 200, 40,40)
level1_enemies.append(inim1)
level1_enemies.append(inim2)
level1_enemies.append(inim3)
level1_enemies.append(inim4)
level1_enemies.append(inim5)
level1_enemies.append(inim6)
level1_enemies.append(inim7)
level1_enemies.append(inim8)
level1_enemies.append(inim9)
level1_enemies.append(inim10)
level1_enemies.append(inim11)
while running:
    
    player_pos = pygame.Vector2(100, screen.get_height() / 2)
    while nivel1 == True:
        player = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nivel1 = False


        screen.fill("purple")

        pygame.draw.circle(screen, "red", player_pos, 20)
        pygame.draw.rect(screen, "green", pygame.Rect(0, 0, 200,400))
        pygame.draw.rect(screen, "green", pygame.Rect(200, 0, 1400,200))
        pygame.draw.rect(screen, "green", pygame.Rect(200, 800, 1400,200))
        pygame.draw.rect(screen, "green", pygame.Rect(0, 600, 200,400))
        pygame.draw.rect(screen, "green", pygame.Rect(1600, 0 , 200,400))
        pygame.draw.rect(screen, "green", pygame.Rect(1600, 600, 200,400))
        pygame.draw.rect(screen, "blue", pygame.Rect(1700, 400, 100,200))
        
        
        for enemy in level1_enemies:
            
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        
        
        pygame.display.flip()


        dt = clock.tick(60) / 1000
        
        i f



    pygame.quit()