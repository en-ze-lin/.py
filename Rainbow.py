import pygame
pygame.init()
size = (700, 500)
LIGHTBLUE = (135, 206, 235)
RED = (255, 0, 0)
ORANGE = (242, 133, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("/Users/enzelin/Desktop/Python/Lesson 4/Rainbow.py")
done = False
clock = pygame.time.Clock()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(LIGHTBLUE)
    pygame.draw.arc(screen, PURPLE, [100, 200, 300, 300], 0, 3, 10)
    pygame.draw.arc(screen, BLUE, [110, 210, 280, 280], 0, 3, 10)
    pygame.draw.arc(screen, GREEN, [120, 220, 260, 260], 0, 3, 10)
    pygame.draw.arc(screen, YELLOW, [130, 230, 240, 240], 0, 3, 10)
    pygame.draw.arc(screen, ORANGE, [140, 240, 220, 220], 0, 3, 10)
    pygame.draw.arc(screen, RED, [150, 250, 200, 200], 0, 3, 10)
    pygame.display.flip()
    clock.tick(600000000000)
pygame.quit()
