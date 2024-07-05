
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
yn = 300
y2n = 700
y = 200
y2 = 760
x = 100
x2 = 100
yp = 500
yp2 = 500
xn = 205
xn2 = 1535
font = pygame.font.Font('freesansbold.ttf', 32)
enemies = [pygame.Rect(400, y, 60,60), pygame.Rect(500, y2, 60,60),
           pygame.Rect(600, y, 60,60), pygame.Rect(700, y2, 60,60),
           pygame.Rect(800, y, 60,60), pygame.Rect(900, y2, 60,60),
           pygame.Rect(1000, y, 60,60), pygame.Rect(1100, y2, 60,60),
           pygame.Rect(1200, y, 60,60), pygame.Rect(1300, y2, 60,60),
           pygame.Rect(1700, 400, 100,200), pygame.Rect(0, 0, 200,400),
           pygame.Rect(200, 0, 1400,200), pygame.Rect(200, 800, 1400,200), 
           pygame.Rect(0, 600, 200,400), pygame.Rect(1600, 0 , 200,400),
           pygame.Rect(1600, 600, 200,400)]


while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    
    while nivel1 == True:
        
        player = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nivel1 = False
                
        screen.fill("white")
        
        player1 = pygame.draw.rect(screen, "red", pygame.Rect( x, yp, 40, 40 ))
        parede1 = pygame.draw.rect(screen, "orange", pygame.Rect(0, 0, 200,400))
        parede2 = pygame.draw.rect(screen, "orange", pygame.Rect(200, 0, 1400,200))
        parede3 = pygame.draw.rect(screen, "orange", pygame.Rect(200, 800, 1400,200))
        parede4 = pygame.draw.rect(screen, "orange", pygame.Rect(0, 600, 200,400))
        parede5 = pygame.draw.rect(screen, "orange", pygame.Rect(1600, 0 , 200,400))
        parede6 = pygame.draw.rect(screen, "orange", pygame.Rect(1600, 600, 200,400))
        meta = pygame.draw.rect(screen, "blue", pygame.Rect(1700, 400, 100,200))
        text = font.render("1º nivel", "black", 'red')
        screen.blit(text, (40, 40))
        
        rect1 = pygame.draw.rect(screen, "black", pygame.Rect(400, y, 60,60))
        rect2 = pygame.draw.rect(screen, "black", pygame.Rect(500, y2, 60,60))
        rect3 = pygame.draw.rect(screen, "black", pygame.Rect(600, y, 60,60))
        rect4 = pygame.draw.rect(screen, "black", pygame.Rect(700, y2, 60,60))
        rect5 = pygame.draw.rect(screen, "black", pygame.Rect(800, y, 60,60))
        rect6 = pygame.draw.rect(screen, "black", pygame.Rect(900, y2, 60,60))
        rect7 = pygame.draw.rect(screen, "black", pygame.Rect(1000, y, 60,60))
        rect8 = pygame.draw.rect(screen, "black", pygame.Rect(1100, y2, 60,60))
        rect9 = pygame.draw.rect(screen, "black", pygame.Rect(1200, y, 60,60))
        rect10 = pygame.draw.rect(screen, "black", pygame.Rect(1300, y2, 60,60))
        rect11 = pygame.draw.rect(screen, "black", pygame.Rect(1400, y, 60,60))
        rect12 = pygame.draw.rect(screen, "black", pygame.Rect(1500, y2, 60,60))
        for enemy in enemies:
            if player1.colliderect(rect1):
                player = False
            if player1.colliderect(rect2):
                player = False
            if player1.colliderect(rect3):
                player = False
            if player1.colliderect(rect4):
                player = False
            if player1.colliderect(rect5):
                player = False
            if player1.colliderect(rect6):
                player = False
            if player1.colliderect(rect7):
                player = False
            if player1.colliderect(rect8):
                player = False
            if player1.colliderect(rect9):
                player = False
            if player1.colliderect(rect10):
                player = False
            if player1.colliderect(rect11):
                player = False
            if player1.colliderect(rect12):
                player = False
            if player1.colliderect(parede1):
                player = False   
            if player1.colliderect(parede2):
                player = False   
            if player1.colliderect(parede3):
                player = False   
            if player1.colliderect(parede4):
                player = False
            if player1.colliderect(parede5):
                player = False   
            if player1.colliderect(parede6):
                player = False      
            if player1.colliderect(meta):
                nivel1 = False   
                screen.fill("white")
                pygame.display.update()
        if y2 <= 200:
            direction2= 'down'
        if y2 >= 740:
            direction2= 'up'
        if direction2 == "down":
            y2 += 10
        if direction2 == "up":
            y2 -=  10 
        if y <= 200:
            direction1= 'down'
        if y >= 740:
            direction1= 'up'
        if direction1 == "down":
            y += 10
        if direction1 == "up":
            y -=  10 

        
            
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            yp -= 300 * dt
        if keys[pygame.K_s]:
            yp += 300 * dt
        if keys[pygame.K_a]:
            x -= 300 * dt
        if keys[pygame.K_d]:
            x += 300 * dt
        
        if player == False:
            x = 100
            yp = 500
        
        pygame.display.flip()


        dt = clock.tick(60) / 1000
    
    if not nivel1:
        nivel2 = True
    while nivel2:
        player = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nivel2 = False
                running = False
        screen.fill("white")

        player1 = pygame.draw.rect(screen, "red", pygame.Rect( x, yp, 40, 40 ))
        parede1 = pygame.draw.rect(screen, "orange", pygame.Rect(0, 0, 200,400))
        parede2 = pygame.draw.rect(screen, "orange", pygame.Rect(200, 0, 1400,200))
        parede3 = pygame.draw.rect(screen, "orange", pygame.Rect(200, 900, 1400,100))
        parede4 = pygame.draw.rect(screen, "orange", pygame.Rect(0, 600, 200,400))
        parede5 = pygame.draw.rect(screen, "orange", pygame.Rect(1600, 0 , 200,400))
        parede6 = pygame.draw.rect(screen, "orange", pygame.Rect(1600, 600, 200,400))
        parede7 = pygame.draw.rect(screen, "orange", pygame.Rect(200, 800, 400,100))
        parede8 = pygame.draw.rect(screen, "orange", pygame.Rect(800, 800, 300,100))
        parede9 = pygame.draw.rect(screen, "orange", pygame.Rect(1300, 800, 300,100))
        
        meta = pygame.draw.rect(screen, "blue", pygame.Rect(1700, 400, 100,200))
        enemies.append(parede7)
        enemies.append(parede8)
        enemies.append(parede9)
        text = font.render("2º nivel", "black", 'red')
        screen.blit(text, (40, 40))
        
        
        rect1 = pygame.draw.rect(screen, "black", pygame.Rect(400, y, 60,60))
        rect2 = pygame.draw.rect(screen, "black", pygame.Rect(500, y, 60,60))
        rect3 = pygame.draw.rect(screen, "black", pygame.Rect(600, y, 60,60))
        rect4 = pygame.draw.rect(screen, "black", pygame.Rect(700, y, 60,60))
        rect5 = pygame.draw.rect(screen, "black", pygame.Rect(800, y, 60,60))
        rect6 = pygame.draw.rect(screen, "black", pygame.Rect(900, y, 60,60))
        rect7 = pygame.draw.rect(screen, "black", pygame.Rect(1000, y, 60,60))
        rect8 = pygame.draw.rect(screen, "black", pygame.Rect(1100, y, 60,60))
        rect9 = pygame.draw.rect(screen, "black", pygame.Rect(1200, y, 60,60))
        rect10 = pygame.draw.rect(screen, "black", pygame.Rect(1300, y, 60,60))
        rect11 = pygame.draw.rect(screen, "black", pygame.Rect(1400, y, 60,60))
        rect12 = pygame.draw.rect(screen, "black", pygame.Rect(1500, y, 60,60))
        for enemy in enemies:
            if player1.colliderect(rect1):
                player = False
            if player1.colliderect(rect2):
                player = False
            if player1.colliderect(rect3):
                player = False
            if player1.colliderect(rect4):
                player = False
            if player1.colliderect(rect5):
                player = False
            if player1.colliderect(rect6):
                player = False
            if player1.colliderect(rect7):
                player = False
            if player1.colliderect(rect8):
                player = False
            if player1.colliderect(rect9):
                player = False
            if player1.colliderect(rect10):
                player = False
            if player1.colliderect(rect11):
                player = False
            if player1.colliderect(rect12):
                player = False
            if player1.colliderect(parede1):
                player = False   
            if player1.colliderect(parede2):
                player = False   
            if player1.colliderect(parede3):
                player = False   
            if player1.colliderect(parede4):
                player = False
            if player1.colliderect(parede5):
                player = False   
            if player1.colliderect(parede6):
                player = False      
            if player1.colliderect(parede7):
                player = False
            if player1.colliderect(parede8):
                player = False          
            if player1.colliderect(parede9):
                player = False        
            if player1.colliderect(meta):
                nivel2 = False   
                nivel1 = False
                screen.fill("white")
                pygame.display.update()
         
        if y <= 200:
            direction1= 'down'
        if y >= 740:
            direction1= 'up'
        if direction1 == "down":
            y += 10
        if direction1 == "up":
            y -=  10

        
            
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            yp -= 300 * dt
        if keys[pygame.K_s]:
            yp += 300 * dt
        if keys[pygame.K_a]:
            x -= 300 * dt
        if keys[pygame.K_d]:
            x += 300 * dt
        
        if player == False:
            x = 100
            yp = 500
        
        pygame.display.flip()


        dt = clock.tick(60) / 1000
      
    if nivel1 == False and nivel2 == False:
        nivel3 = True
    while nivel3 == True:
        font = pygame.font.Font()
        player = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nivel3 = False
                
        screen.fill("white")

        player1 = pygame.draw.rect(screen, "red", pygame.Rect( x, yp, 40, 40 ))
        parede1 = pygame.draw.rect(screen, "orange", pygame.Rect(0, 0, 200,400))
        parede2 = pygame.draw.rect(screen, "orange", pygame.Rect(200, 0, 1400,100))
        parede3 = pygame.draw.rect(screen, "orange", pygame.Rect(200, 900, 1400,100))
        parede4 = pygame.draw.rect(screen, "orange", pygame.Rect(0, 600, 200,400))
        parede5 = pygame.draw.rect(screen, "orange", pygame.Rect(1600, 0 , 200,400))
        parede6 = pygame.draw.rect(screen, "orange", pygame.Rect(1600, 600, 200,400))
        meta = pygame.draw.rect(screen, "blue", pygame.Rect(1700, 400, 100,200))
        
        text = font.render("3º nivel", "black", 'red')
        screen.blit(text, (40, 40))
        
        rect1 = pygame.draw.rect(screen, "black", pygame.Rect(400, yn, 60,60))
        rect2 = pygame.draw.rect(screen, "black", pygame.Rect(500, y2n, 60,60))
        rect3 = pygame.draw.rect(screen, "black", pygame.Rect(600, yn, 60,60))
        rect4 = pygame.draw.rect(screen, "black", pygame.Rect(700, y2n, 60,60))
        rect5 = pygame.draw.rect(screen, "black", pygame.Rect(800, yn, 60,60))
        rect6 = pygame.draw.rect(screen, "black", pygame.Rect(900, y2n, 60,60))
        rect7 = pygame.draw.rect(screen, "black", pygame.Rect(1000, yn, 60,60))
        rect8 = pygame.draw.rect(screen, "black", pygame.Rect(1100, y2n, 60,60))
        rect9 = pygame.draw.rect(screen, "black", pygame.Rect(1200, yn, 60,60))
        rect10 = pygame.draw.rect(screen, "black", pygame.Rect(1300, y2n, 60,60))
        rect11 = pygame.draw.rect(screen, "black", pygame.Rect(1400, yn, 60,60))
        rect12 = pygame.draw.rect(screen, "black", pygame.Rect(1500, y2n, 60,60))
        rect13 = pygame.draw.rect(screen, "black", pygame.Rect(xn, 105, 60,60))
        rect14 = pygame.draw.rect(screen, "black", pygame.Rect(xn2, 205, 60,60))
        rect15 = pygame.draw.rect(screen, "black", pygame.Rect(xn, 735, 60,60))
        rect16 = pygame.draw.rect(screen, "black", pygame.Rect(xn2, 835, 60,60))

        for enemy in enemies:
            if player1.colliderect(rect1):
                player = False
            if player1.colliderect(rect2):
                player = False
            if player1.colliderect(rect3):
                player = False
            if player1.colliderect(rect4):
                player = False
            if player1.colliderect(rect5):
                player = False
            if player1.colliderect(rect6):
                player = False
            if player1.colliderect(rect7):
                player = False
            if player1.colliderect(rect8):
                player = False
            if player1.colliderect(rect9):
                player = False
            if player1.colliderect(rect10):
                player = False
            if player1.colliderect(rect11):
                player = False
            if player1.colliderect(rect12):
                player = False
            if player1.colliderect(parede1):
                player = False   
            if player1.colliderect(parede2):
                player = False   
            if player1.colliderect(parede3):
                player = False   
            if player1.colliderect(parede4):
                player = False
            if player1.colliderect(parede5):
                player = False   
            if player1.colliderect(parede6):
                player = False      
            if player1.colliderect(meta):
                nivel1 = False   
                screen.fill("white")
                pygame.display.update()
        if y2n <= 300:
            direction2= 'down'
        if y2n >= 700:
            direction2= 'up'
        if direction2 == "down":
            y2n += 8
        if direction2 == "up":
            y2n -=  8 
        if yn <= 300:
            direction1= 'down'
        if yn >= 700  :
            direction1= 'up'
        if direction1 == "down":
            yn += 8
        if direction1 == "up":
            yn -=  8
        
        if xn2 <= 205:
            direction3= 'right'
        if xn2 >= 1535:
            direction3= 'left'
        if direction3 == "right":
            xn2 += 8
        if direction2 == "left":
            xn2 -=  8 
        if xn <= 300:
            direction1= 'down'
        if xn >= 700  :
            direction1= 'up'
        if direction1 == "down":
            xn += 8
        if direction1 == "up":
            xn -=  8
        
            
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            yp -= 300 * dt
        if keys[pygame.K_s]:
            yp += 300 * dt
        if keys[pygame.K_a]:
            x -= 300 * dt
        if keys[pygame.K_d]:
            x += 300 * dt
        
        if player == False:
            x = 100
            yp = 500
        
        pygame.display.flip()


        dt = clock.tick(60) / 1000
    

    if nivel1 == False and nivel2 == False and nivel3 == False:
        running = False