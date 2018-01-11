import pygame, random, time, sys
from pygame.locals import *
#display setup

display_width = d_w = 600 
display_height = d_h = 500

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Memory Game') 
clock = pygame.time.Clock()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#grid
pos_1 = d_w * 0.75
pos_2 = d_w * 0.5
pos_3 = d_w * 0.25

pos_4 = d_h * 0.66
pos_5 = d_h * 0.33


pos_x = [pos_1,pos_2,pos_3]
pos_y = [pos_4,pos_5]

def getRandomX():
    rand_x = pos_x[random.randrange(len(pos_x))]
    return(rand_x)
    pygame.display.update()

def getRandomY():
    rand_y = pos_y[random.randrange(len(pos_y))]
    return(rand_y)
    pygame.display.update()


#cards
cupImg = pygame.image.load("cup.png").convert_alpha()
drinkImg = pygame.image.load("drink.png").convert_alpha()
cupImg_rect = cupImg.get_rect()
drinkImg_rect = drinkImg.get_rect()


def cup(rand_x,rand_y):
    global cupImg_rect
    cupImg_rect.x = rand_x
    cupImg_rect.y = rand_y
    gameDisplay.blit(cupImg,cupImg_rect)

def drink(rand_x,rand_y):
    global drinkImg_rect
    drinkImg_rect.x = rand_x
    drinkImg_rect.y = rand_y
    gameDisplay.blit(drinkImg,(rand_x,rand_y))

#test area
def second_press():
    if drinkImg_rect.collidepoint(pos) and pressed1:
        print("point")
    elif cupImg_rect.collidepoint(pos) and pressed1:
        print("no_point")
    else:
        print("error")
        
def second_press_2():
    if drinkImg_rect.collidepoint(pos) and pressed1:
        print("no_point")
    elif cupImg_rect.collidepoint(pos) and pressed1:
        print("point")
    else:
        print("error")
    
#game loop
running = True

cup_x = getRandomX()
cup_y = getRandomY()
drink_x = getRandomX()
drink_y = getRandomY()

while running:
    
    pos = pygame.mouse.get_pos()
    #pressed1 = pygame.mouse.get_pressed()
    #print("pos: {0}\nPressed: {1}",pos,pressed1)
    #if drinkImg_rect.collidepoint(pos) and pressed1[0]:
    #    print("point")
    #elif cupImg_rect.collidepoint(pos) and pressed1:
    #    print("point")
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("pressed mouse")
            print("mousePos: ",event.pos,"\nRect: ",drinkImg_rect)
            if drinkImg_rect.collidepoint(event.pos):
                print("point")
    #print(event)

    
        
    gameDisplay.fill(white)

    cup(cup_x,cup_y)
    drink(drink_x,drink_y)
    
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
exit()
