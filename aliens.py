import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Aliens coming")

x = 50
y = 50
widht = 40
height = 60
speed = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - widht - 5:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    win.fill((0,0,0))
    pygame.draw.rect(win, (153, 0, 0,), (x, y, widht, height))
    pygame.display.update()

pygame.quit()