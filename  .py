import pygame
import random
import time
pygame.init()
screen_width = 700
screen_height = 400
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,0   ,0   )
GREEN = (245, 2, 94)
BLUE = (0, 255, 0)

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("🧪2️⃣ScienceLab2 - Collision")
player_x = 0
player_y = 0
player_w = 25
player_h = 25
block_w = 25
block_h = 25
block_x = []
block_y = []
collision = []
score = 0
count = 0
for a in range(20):
        block_x.append(random.randrange(0, screen_width - block_w))
        block_y.append(random.randrange(0, screen_height - block_h))
        collision.append(False)
font = pygame.font.Font("/Users/enzelin/Desktop/Python/Blackboysonmopeds.ttf", 50)
start_ticks = pygame.time.get_ticks()
done = False
clock = pygame.time.Clock()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    seconds = int((pygame.time.get_ticks() - start_ticks)/1000)
    pos = pygame.mouse.get_pos()
    player_x = pos[0]
    player_y = pos[1]
    pygame.draw.rect(screen, RED, [player_x, player_y, player_w, player_h])
    for a in range(0, 20):
        if collision[a] == False:
            
            pygame.draw.rect(screen, BLACK, [block_x[a], block_y[a], block_w, block_h])
    for a in range(0, 20):
        yin = block_y[a] <= player_y <= block_y[a] + block_h or block_y[a] <= player_y + player_h <= block_y[a] + block_h
        xin = block_x[a] <= player_x <= block_x[a] + block_w or block_x[a] <= player_x + player_w <= block_x[a] + block_w
        if xin == True and yin == True and collision[a] == False:
            collision[a] = True
            score = score + 1
    if score >= 20:
        text = font.render("Good t ing, y u FAIL to fail.", 10, BLUE)
        screen.blit(text, (100, 100))
        done = True
    if seconds > 20:
        text = font.render("gane over resut: Losery", 10, RED)
        done = True
        
       
        screen.blit(text, (100, 100))
    message = str(score) + ".00p oi t"
    text = font.render(message, True, BLACK)
    screen.blit(text, (4, 10))
    time_text = font.render("you 're t me;" + str(seconds) , 1, GREEN)
    screen.blit(time_text, (4, 30))
    pygame.display.flip()
    clock.tick(random.randrange(0, 140))
time.sleep(3)
pygame.quit()
