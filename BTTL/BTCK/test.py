import pygame
from random import randint

pygame.init()
screen_width, screen_height = 400, 600
screen = pygame.display.set_mode((screen_width, screen_height))
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
running = True
clock = pygame.time.Clock()

 

TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 150

 

tube1_x = 600
tube2_x = 800
tube3_x = 1000

 

tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)

 

tube1_pass = False
tube2_pass = False
tube3_pass = False

 

score = 0

 

BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 55
BIRD_HEIGHT = 55
bird_drop_velocity = 0
GRAVITY = 0.5
pausing = False

 

font = pygame.font.SysFont('sans', 30)

 

background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (screen_width + 500, screen_height))
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))

 

while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(background_img, (0, 0))

 

tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))

 

tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH, screen_height - tube1_height - TUBE_GAP))
tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, screen_height - tube2_height - TUBE_GAP))
tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, screen_height - tube3_height - TUBE_GAP))

 

tube1_x = tube1_x - TUBE_VELOCITY
tube2_x = tube2_x - TUBE_VELOCITY
tube3_x = tube3_x - TUBE_VELOCITY

 

bird_rect = screen.blit(bird_img, (BIRD_X, bird_y))

 

bird_y += bird_drop_velocity
bird_drop_velocity += GRAVITY

 

if tube1_x < -50:
    tube1_x = 550
tube1_pass = False
tube1_height = randint(100, 400)
if tube2_x < -50:
    tube2_x = 550
tube2_pass = False
tube2_height = randint(100, 400)
if tube3_x < -50:
    tube3_x = 550
tube3_pass = False
tube3_height = randint(100, 400)

 

score_txt = font.render("Score: " + str(score), True, BLACK)
screen.blit(score_txt, (0, 0))

 

if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
    score += 1
tube1_pass = True
if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
    score += 1
tube2_pass = True
if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
    score += 1
tube3_pass = True

 

for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube2_rect_inv]:
    if bird_rect.colliderect(tube):
        TUBE_VELOCITY = 0
        bird_drop_velocity = 0
        pausing = True

 

if bird_y > 600:
    TUBE_VELOCITY = 0
bird_drop_velocity = 0
pausing = True

 

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        if pausing:
            bird_y = 400
TUBE_VELOCITY = 3
tube1_x = 600
tube2_x = 800
tube3_x = 1000
score = 0
pausing = False

 

bird_drop_velocity = 0
bird_drop_velocity -= 10

 

pygame.display.flip()
pygame.quit()