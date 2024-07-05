import pygame 
# Only import the things you need it makes debugging and documenting 
# alot easier if you know where everything is coming from 
from pygame.locals import QUIT 
FPS = 70

# Use variables to define width and height in case you want to 
# change it later 
width = 200
height = 200

# I would group variables by usage, for example, I would group width, 
# height of the screen and w, h of the box so I can easily manipulate 
# the numbers if want to.
w = 50
h = 60

# Using an offset variable reduces the hardcoded numbers even more 
# if its 0 it will just move along the border but if it >0 it will move 
# the square to the centre
offset = 20

# You can declare it as a variable if you need the SIZE tuple somewhere 
# else, if you don't need it you can just set it as 
# pygame.display.set_mode((width, height))
SIZE = (width, height)
WHITE = (255, 255, 255)
RED =  (255, 0, 0)

x = offset
y = offset
direction = 'down'

# This is just my preference but I like to have the variables that are 
# changeable at the top for easy access. I think this way the code is 
# cleaner.
pygame.init()
fpsclock = pygame.time.Clock()
form1 = pygame.display.set_mode(SIZE)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    form1.fill(WHITE)

    # Try to avoid hardcoded numbers as much as possible, hardcoded 
    # numbers are hard to change later on when the code gets to certain 
    # size and complexity. 
    pygame.draw.rect(form1, RED, (x, y, w, h), 1)
    pygame.display.update()
    fpsclock.tick(FPS)

    # Don't harcode conditions, use variables so you can easily change 
    # them later
    if x == offset and y == offset:
        direction='right'
    if x == width - w - offset and y == offset:
        direction='down'
    if x == width - w - offset and y == height - h - offset:
        direction='left'
    if x == offset and y == height - h - offset:
        direction='up'

    elif direction == 'down':
      #Keep in mind going down actually means to increment y
      y += 5
    
    elif direction == 'up':
      y -= 5
   
        inim3 = pygame.draw.rect(screen, "black", pygame.Rect(600, 200, 40,40))
        inim4 = pygame.draw.rect(screen, "black", pygame.Rect(700, y2, 40,40))
        inim5 = pygame.draw.rect(screen, "black", pygame.Rect(800, 200, 40,40))
        inim6 = pygame.draw.rect(screen, "black", pygame.Rect(900, y2, 40,40))
        inim7 = pygame.draw.rect(screen, "black", pygame.Rect(1000, 200, 40,40))
        inim8 = pygame.draw.rect(screen, "black", pygame.Rect(1100, y2, 40,40))
        inim9 = pygame.draw.rect(screen, "black", pygame.Rect(1200, 200, 40,40))
        inim10 = pygame.draw.rect(screen, "black", pygame.Rect(1300, y2, 40,40))
        inim11 = pygame.draw.rect(screen, "black", pygame.Rect(1400, 200, 40,40))

