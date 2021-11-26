import pygame
import random
from queue import Queue
BLACK = (6, 6, 110)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
segment_width = 15
segment_height = 15
segment_margin = 3
segment_head_x = 0
segment_head_y = 0
grid_x = segment_width + segment_margin
grid_y = segment_height + segment_margin
pygame.display.set_caption("🐍Snake mini")
x_change = 1
y_change = 0
class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x * grid_x
        self.rect.y = y * grid_y   
        self.x = x
        self.y = y
pygame.init()
screen_height = 300
screen_width = 400
screen = pygame.display.set_mode([screen_width, screen_height])
alllist = pygame.sprite.Group()
snake_segments = Queue()
for i in range(0, 3):
    x = 3 + i
    y = 3 
    segment = Segment(x, y)
    snake_segments.put(segment)
    alllist.add(segment)
    segment_head_x = x
    segment_head_y = y
    print(i, segment.x, segment.y)
done = False
eat = True
score = 0
font = pygame.font.Font("/Users/enzelin/Desktop/Python/calculatrix-12.ttf", 20)
clock = pygame.time.Clock()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 1
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 1
    if eat:
        xa = random.randrange(20)
        ya = random.randrange(15)
        eat = False
    else:
        old_segment = snake_segments.get()
        alllist.remove(old_segment)
    segment_head_x = segment_head_x + x_change
    segment_head_y = segment_head_y + y_change
    apple = Segment(xa, ya)
    segment = Segment(segment_head_x, segment_head_y)
    snake_segments.put(segment)
    alllist.add(segment)
    if segment.x == apple.x and segment.y == apple.y:
        eat = True
        score = score + 1
    screen.fill(BLACK)
    text = font.render(str(score) + " point", 10, WHITE)
    screen.blit(text, (10, 10))
    pygame.draw.rect(screen, RED, (xa*grid_x, ya*grid_y, segment_width, segment_height))
    alllist.draw(screen)
    pygame.display.flip()
    clock.tick(3)
pygame.quit()