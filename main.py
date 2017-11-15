import pygame
#display setup

display_width = 600
display_height = 500

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Open the dungeon') 
clock = pygame.time.Clock()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#cards
drinkImg = pygame.image.load("dinks.png")
def drink(x,y):
    gameDisplay.blit(drinkImg,(x,y))
    
cupImg = pygame.image.load("cup.png")
def cup(x_c,y_c):
    gameDisplay.blit(cupImg,(x_c,y_c))
    
#positions    
x = (display_width * 0.15)
y = (display_height * 0.001)

x_c = (x + (d_w /(random.randint(2, 4))))
y_c = (x + 5)

x_d = (x + (d_w /(random.randint(2, 4))))
y_d = (x + 70)
    
#game loop
crashed = False

while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = False

    print(event)
#object update        
    gameDisplay.fill(black)
    drink(x,y)
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
