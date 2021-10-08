import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("/Users/enzelin/Desktop/Python/Lesson 3/ship.py")
BG_pos = [0, 0]
pygame.mixer.music.load("Mario.mp3")
BG_image = pygame.image.load("/Users/enzelin/Desktop/Python/Lesson 3/maxresdefault.jpeg").convert()
player_image = pygame.image.load("/Users/enzelin/Desktop/Python/Lesson 3/mario-1.png").convert()
player_image.set_colorkey(BLACK)
done = False
pygame.mixer.music.play()
clock = pygame.time.Clock()
x = 0
y = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(BG_image, BG_pos)
    player_pos = [x, y]
    screen.blit(player_image, player_pos)
    keys = pygame.key.get_pressed()   
    if keys[pygame.K_LEFT]:
                x -= 4
    if keys[pygame.K_RIGHT]:
                x += 4
    if keys[pygame.K_UP]:
                y -= 4
    if keys[pygame.K_DOWN]:
                y += 4
    #x = player_pos[0]
    #y = player_pos[1]
    pygame.display.flip()
    clock.tick(60)
pygame.quit()