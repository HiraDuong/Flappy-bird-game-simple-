'''
1. Vẽ ống
2. Vẽ chim
3. Tính điểm
4. Dừng màn hình
'''


import pygame
from random import randint
pygame.init()
WIDTH,HEIGHT = 400,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Flappy Bird')
running = True
pausing = False

GREEN = ( 0,200,0)
BLUE = (0,0,255)
RED = (255,0,0)
LIGHT_BLUE = (100,100,255)
YELLOW = (255,255,0)

clock = pygame.time.Clock()
TUBE_VELOCITY = 2
TUBE_GAB = 150
TUBE_WIDTH = 50
BIRD_VELOC_DROP = 0

score = 0
font = pygame.font.SysFont('sans', 20)

tube1_x=600 
tube2_x=800
tube3_x=1000
bird_x = 50
bird_y = 300
bird_width = 30
bird_img = pygame.image.load("D:/NEWCODE/Game learning/flappy_bird/bird.png")
bird_img = pygame.transform.scale(bird_img,(bird_width,bird_width))
background_img = pygame.image.load("D:/NEWCODE/Game learning/flappy_bird/background.png")

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

tube1_pass = False
tube2_pass = False
tube3_pass = False

while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(background_img,(0,0))
    #DRAW TUBE
    tube1_rect =pygame.draw.rect(screen,BLUE,(tube1_x,0,TUBE_WIDTH,tube1_height))
    tube2_rect =pygame.draw.rect(screen,BLUE,(tube2_x,0,TUBE_WIDTH,tube2_height))
    tube3_rect =pygame.draw.rect(screen,BLUE,(tube3_x,0,TUBE_WIDTH,tube3_height))
    
    #DRAW INVERSE TUBE
    tube1_inverse_rect = pygame.draw.rect(screen,BLUE,(tube1_x,tube1_height+TUBE_GAB,TUBE_WIDTH,HEIGHT - (tube1_height-TUBE_GAB)))
    tube2_inverse_rect = pygame.draw.rect(screen,BLUE,(tube2_x,tube2_height+TUBE_GAB,TUBE_WIDTH,HEIGHT - (tube2_height-TUBE_GAB)))
    tube3_inverse_rect = pygame.draw.rect(screen,BLUE,(tube3_x,tube3_height+TUBE_GAB,TUBE_WIDTH,HEIGHT - (tube3_height-TUBE_GAB)))
    # TUBE TO LEFT  
    tube1_x = tube1_x- TUBE_VELOCITY
    tube2_x = tube2_x- TUBE_VELOCITY
    tube3_x = tube3_x- TUBE_VELOCITY
    #CREATE NEW TUBE
    if tube1_x<-TUBE_WIDTH :
        tube1_x = 550
        tube1_height = randint(100,400)
        tube1_pass = False
    if tube2_x<-TUBE_WIDTH :
        tube2_x = 550   
        tube2_height = randint(100,400) 
        tube2_pass = False
    if tube3_x<-TUBE_WIDTH :
        tube3_x = 550
        tube3_height = randint(100,400)
        tube3_pass = False
    #DRAW BIRD
    #bird_rect = pygame.draw.rect(screen,RED,(bird_x,bird_y,bird_width,bird_width))
    bird_rect = screen.blit(bird_img,(bird_x,bird_y))
    #BIRD DROP
    bird_y+=BIRD_VELOC_DROP
    BIRD_VELOC_DROP +=0.1


 #DRAW POINT BOX
    pygame.draw.rect(screen,LIGHT_BLUE,(0,0,100,50))
    scores = "Scores : " + str(score)  
    screen.blit(font.render(scores,True,RED),(0,0))
 
    #UPDATE POINT
    if (tube1_x + TUBE_WIDTH) <= bird_x and tube1_pass == False:
        score+=1
        tube1_pass= True
    if (tube2_x + TUBE_WIDTH) <= bird_x and tube2_pass == False:
        score+=1
        tube2_pass= True
    if (tube3_x + TUBE_WIDTH) <= bird_x and tube3_pass == False:
        score+=1
        tube3_pass= True
    #DRAW SAND
    sand_rect =pygame.draw.rect(screen,YELLOW,(0,600-10,WIDTH,10))

    #GAME OVER
    #check collision 
    '''
    if bird_rect.colliderect(tube1_rect):
        TUBE_VELOCITY = 0
        pausing = True
    if bird_rect.colliderect(tube2_rect):
        TUBE_VELOCITY = 0
        pausing = True
    if bird_rect.colliderect(tube3_rect):
        TUBE_VELOCITY = 0
        pausing = True
    '''
    for tube in [tube1_rect,tube2_rect,tube3_rect,tube1_inverse_rect,tube2_inverse_rect,tube3_inverse_rect,sand_rect] :
        if bird_rect.colliderect(tube):
            pausing = True
            TUBE_VELOCITY = 0
            BIRD_VELOC_DROP = 0
            pygame.draw.rect(screen,YELLOW,(WIDTH/2-150,HEIGHT/2-100,300,200))
            
            game_over_txt = font.render("Game Over ! Score : " + str(score),True,RED)
            screen.blit(game_over_txt,(WIDTH/2-50,HEIGHT/2))
            game_continue_txt = font.render("Press Space to continue ",True,RED)
            screen.blit(game_continue_txt,(WIDTH/2 -50,HEIGHT/2 +50))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pausing:
                    score = 0
                    TUBE_VELOCITY = 2
                    bird_x = 50
                    bird_y = 300
                    tube1_x = 600
                    tube2_x = 800
                    tube3_x = 1000
                    pausing = False
                BIRD_VELOC_DROP = 0
                BIRD_VELOC_DROP -=3
    pygame.display.flip()
pygame.quit()