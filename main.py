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

#images

#game loop
crashed = False

while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = False

        print(event)
        
    gameDisplay.fill(black)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
