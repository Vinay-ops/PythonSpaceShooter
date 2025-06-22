import pygame
import random

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Space Shooter")

Background = pygame.image.load("Background.jpg")
Background = pygame.transform.scale(Background, (800, 800))

Player = pygame.image.load("Spaceship.png")
Player = pygame.transform.scale(Player, (100, 100))

Bullet = pygame.image.load("Bullet.png")
Bullet = pygame.transform.scale(Bullet, (20, 40))

Enemy = pygame.image.load("Enemy.png")
Enemy = pygame.transform.scale(Enemy, (80, 80))
Enemy = pygame.transform.rotate(Enemy, 180)

Playerinx = 300
Playeriny = 600

Bullets = []
Bulletspeed = 5
can_shoot = True

font = pygame.font.SysFont("Arial", 30)
score = 0

Enemyx = random.randint(0, 620)
Enemyy = -80
Enemyspeed = 0.3 

def show_score():
    score_text = font.render("Score: " + str(score), True, (250, 250, 250))
    screen.blit(score_text, (550, 20))

def is_collision(Enemyx, Enemyy, Bulletinx, Bulletiny):
    distance = ((Enemyx - Bulletinx)**2 + (Enemyy - Bulletiny)**2) ** 0.5
    return distance < 50

running = True
while running:
    screen.blit(Background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and Playerinx > 0:
        Playerinx -= 0.5
    if keys[pygame.K_RIGHT] and Playerinx < 600:
        Playerinx += 0.5
    if keys[pygame.K_UP] and Playeriny > 0:
        Playeriny -= 1
    if keys[pygame.K_DOWN] and Playeriny < 600:
        Playeriny += 1

    if keys[pygame.K_SPACE] and can_shoot:
        Bulletinx = Playerinx + 45
        Bulletiny = Playeriny
        Bullets.append([Bulletinx, Bulletiny])
        can_shoot = False

    if not keys[pygame.K_SPACE]:
        can_shoot = True

    for B in Bullets:
        B[1] -= Bulletspeed
    Bullets = [B for B in Bullets if B[1] > -20]

    Enemyy += Enemyspeed
    if Enemyy > 700:
        Enemyx = random.randint(0, 620)
        Enemyy = -80

    for B in Bullets:
        if is_collision(Enemyx + 30, Enemyy + 30, B[0], B[1]):
            score += 1
            Bullets.remove(B)
            Enemyx = random.randint(0, 620)
            Enemyy = -80
            break

    screen.blit(Player, (Playerinx, Playeriny))
    for B in Bullets:
        screen.blit(Bullet, (B[0], B[1]))
    screen.blit(Enemy, (Enemyx, Enemyy))
    show_score()

    pygame.display.flip()

pygame.quit()
