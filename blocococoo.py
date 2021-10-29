import pygame
import random
pygame.init()
screen_width = 700
screen_height = 400
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,0   ,0   )
player_image = pygame.image.load("/Users/enzelin/Desktop/Python/Lesson 6/skull2.png")
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("/Users/enzelin/Desktop/Python/Lesson 6/skull2.png").convert()
        self.rect = self.image.get_rect()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Virus.exe")
block_list = pygame.sprite.Group()
all_list = pygame.sprite.Group()
for i in range(0, 50):
                block = Block()
                block.rect.x = random.randrange(0, screen_width)
                block.rect.y = random.randrange(0, screen_height)
                all_list.add(block)
        
done = False
clock = pygame.time.Clock()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(RED)

    player_pos = pygame.mouse.get_pos()
    x = player_pos[0]
    y = player_pos[1]
    screen.blit(player_image, [x, y])

   
    all_list.draw(screen)
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
