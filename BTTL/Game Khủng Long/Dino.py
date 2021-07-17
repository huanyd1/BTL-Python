import pygame
pygame.init()
#Xết màn hình
screen = pygame.display.set_mode((900,300))
pygame.display.set_caption('Dino Game')
#Màu RGB
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
#Xét tọa độ
backgroundScaleX = 0
backgroundScaleY = 0
dinoScaleX = 0
dinoScaleY = 230
# dino_bowScaleX = 0
# dino_bowScaleY = 200
treeScaleX = 550
treeScaleY = 230
doubleTreeScaleX = 800
doubleTreeScaleY = 230
birdScaleX = 1300
birdScaleY = 230
x_speed = 5
y_seed = 7
jump = False
pausing = False
#Tạo âm thanh
soundJump = pygame.mixer.Sound('D:/Python/BTTL/Game Khủng Long/Audio/jump.wav')
soundEndGame = pygame.mixer.Sound('D:/Python/BTTL/Game Khủng Long/Audio/ting.wav')
#Tạo điểm
score = 0
hight_score = 0
font = pygame.font.SysFont('time',20)
font_endgame = pygame.font.SysFont('time',40)
#Load ảnh background
background = pygame.image.load('D:/Python/BTTL/Game Khủng Long/Images/background.jpg')
dino = pygame.image.load('D:/Python/BTTL/Game Khủng Long/Images/dino.jpg')
tree = pygame.image.load('D:/Python/BTTL/Game Khủng Long/Images/tree.png')
doubletree = pygame.image.load('D:/Python/BTTL/Game Khủng Long/Images/double-tree.png')
bird = pygame.image.load('D:/Python/BTTL/Game Khủng Long/Images/bird.png')
clock = pygame.time.Clock()
running = True
while running:
    #Xét tốc độ nháy -- nếu k có sẽ nháy theo tốc độ tối đa máy tính
    clock.tick(60)
    screen.fill(WHITE)
    #Xét Background
    background_rect_start = screen.blit(background,(backgroundScaleX, backgroundScaleY))
    background_rect_end = screen.blit(background,(backgroundScaleX + 600, backgroundScaleY))
    score_text = font.render("Score: "+str(score), True, BLACK)
    hight_score_text = font.render("Hight Score: "+str(hight_score), True, RED)
    screen.blit(score_text,(5,5))
    screen.blit(hight_score_text,(5,20))
    #Xét tọa độ
    dino_rect = screen.blit(dino,(dinoScaleX,dinoScaleY))
    tree_rect = screen.blit(tree,(treeScaleX,treeScaleY))
    doubletree_rect = screen.blit(doubletree,(doubleTreeScaleX,doubleTreeScaleY))
    bird_rect = screen.blit(bird,(birdScaleX,birdScaleY))
    #Xét backgroud vượt màn hình
    if backgroundScaleX + 600 <= 0:
        backgroundScaleX = 0
    #Xét cây vượt qua màn hình
    treeScaleX = treeScaleX - x_speed
    if treeScaleX <= 20:
        treeScaleX = 550
        score =  score + 1
    #Xét 2 cây vượt qua màn hình
    doubleTreeScaleX = doubleTreeScaleX - x_speed
    if doubleTreeScaleX <= 20:
        doubleTreeScaleX = 800
        score =  score + 1
    birdScaleX = birdScaleX - x_speed
    if birdScaleX <= 20:
        birdScaleX = 1300
        score =  score + 1
    #Kiểm tra tọa độ của Dino
    if 230 >= dinoScaleY >= 80:
        if jump == True:
            dinoScaleY = dinoScaleY - y_seed
    else:
        jump = False
    #Xét Dino rơi xuống
    if dinoScaleY < 230:
        if jump == False:
            dinoScaleY = dinoScaleY + y_seed
    #Tăng level
    # if score %3 == 0:
    #     x_speed += 1
    #Kiểm tra va chạm
    if dino_rect.colliderect(tree_rect):
        pygame.mixer.Sound.play(soundEndGame)
        pausing = True
        gameover_text = font_endgame.render("GAME OVER", True, RED)
        screen.blit(gameover_text,(350,150))
        x_speed = 0
        y_seed = 0

        if score > hight_score:
            hight_score = score
    if dino_rect.colliderect(doubletree_rect):
        pygame.mixer.Sound.play(soundEndGame)
        pausing = True
        gameover_text = font_endgame.render("GAME OVER", True, RED)
        screen.blit(gameover_text,(350,150))
        x_speed = 0
        y_seed = 0

        if score > hight_score:
            hight_score = score
    if dino_rect.colliderect(bird_rect):
        pygame.mixer.Sound.play(soundEndGame)
        pausing = True
        gameover_text = font_endgame.render("GAME OVER", True, RED)
        screen.blit(gameover_text,(350,150))
        x_speed = 0
        y_seed = 0
        if score > hight_score:
            hight_score = score
    backgroundScaleX = backgroundScaleX  - x_speed
    #Lấy sự kiện trong Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dinoScaleY == 230:
                    pygame.mixer.Sound.play(soundJump)
                    jump = True
                if pausing:
                    score = 0
                    backgroundScaleX = 0
                    backgroundScaleY = 0
                    dinoScaleX = 0
                    dinoScaleY = 230
                    treeScaleX = 550
                    treeScaleY = 230
                    x_speed = 5
                    y_seed = 7
                    pausing = False

    pygame.display.flip()
pygame.quit()