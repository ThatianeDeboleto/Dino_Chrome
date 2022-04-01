import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Jump Debolete's")
myfont = pygame.font.SysFont('Arial', 16)

y = 310
score = 1
speed = 2
enemy = False
enemy_x = 590
game_over = False

run = True
while run:
    if (random.randint(0, 400) == 42 and enemy == False):
        enemy = True

    pygame.time.delay(speed)
    if (game_over == False):
        score += 1
    else:
        enemy = False
    textsurface = myfont.render('Pontos: ' + str(score), False, (0, 0, 0))
    logo = myfont.render('Jump Deboleto', False, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if (game_over == True):
            game_over = False
            enemy = False
            enemy_x = 590
            score = 0
        for i in range(128):
            score += 1
            y -= 1
            pygame.time.delay(speed)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (255, 0, 0), (20, y, 50, 50))
            textsurface = myfont.render('Pontos: ' + str(score), False, (0, 0, 0))
            logo = myfont.render('Jump Deboleto', False, (0, 0, 0))
            screen.blit(textsurface, (0, 20))
            screen.blit(logo, (0, 0))

            if (enemy == True):
                if (y > 260 and enemy_x < 70):
                    game_over = True
                pygame.draw.rect(screen, (0, 255, 0), (enemy_x, 310, 50, 50))
                enemy_x -= 1
                if (enemy_x == 0):
                    enemy = False
                    enemy_x = 590

            pygame.display.update()
        for i in range(128):
            score += 1
            y += 1
            pygame.time.delay(speed)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (255, 0, 0), (20, y, 50, 50))
            textsurface = myfont.render('Pontos: ' + str(score), False, (0, 0, 0))
            logo = myfont.render('Jump Deboleto', False, (0, 0, 0))
            screen.blit(textsurface, (0, 20))
            screen.blit(logo, (0, 0))

            if (enemy == True):
                if (y > 260 and enemy_x < 70):
                    game_over = True
                pygame.draw.rect(screen, (0, 255, 0), (enemy_x, 310, 50, 50))
                enemy_x -= 1
                if (enemy_x == 0):
                    enemy = False
                    enemy_x = 590

            pygame.display.update()
    screen.fill((255, 255, 255))
    screen.blit(logo, (0, 0))
    screen.blit(textsurface, (0, 20))
    if (game_over == True):
        game_over_text = myfont.render('Fim de Jogo', False, (0, 0, 0))
        screen.blit(game_over_text, (0, 40))
    pygame.draw.rect(screen, (255, 0, 0), (20, y, 50, 50))

    if (enemy == True):
        if (y > 260 and enemy_x < 100):
            game_over = True
        pygame.draw.rect(screen, (0, 255, 0), (enemy_x, 310, 50, 50))
        enemy_x -= 1
        if (enemy_x == 0):
            enemy = False
            enemy_x = 590

    pygame.display.update()
pygame.display.quit()