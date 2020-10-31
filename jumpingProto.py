import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jump Game")

x = 200
y = 200
width = 30
height = 40
isjump = False
v = 10
m = 1
run = True

while run:

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if isjump == False:
        if keys[pygame.K_SPACE]:
            isjump = True

    if isjump:
        F = (1 / 2) * m * (v ** 2)

        y -= F
        v = v - 1

        if v < 0:
            m = -1

        if v == -11:
            isjump = False

            v = 10
            m = 1


    pygame.time.delay(20)
    pygame.display.update()

pygame.quit()
