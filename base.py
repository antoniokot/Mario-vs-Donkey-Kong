import pygame as pg

print('Use WASD e as setas do teclado para movimentar os quadrados!')

done = False
cor1 = (155,200,0)
cor2 = (100,50,200)
cor3 = (120, 90, 100)

direcao1 = [0,0]
direcao2 = [260,260]

pg.init()
screen = pg.display.set_mode((300,300))

while not done:
    

    for event in pg.event.get():
        screen.fill((0, 0, 0))
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                if direcao1[0] >= 5:
                    direcao1[0] -= 5
            if event.key == pg.K_d:
                if direcao1[0] <= 255:
                    direcao1[0] += 5
            if event.key == pg.K_s:
                if direcao1[1] <= 255:
                    direcao1[1] += 5
            if event.key == pg.K_w:
                if direcao1[1] >= 5:
                    direcao1[1] -= 5

            if event.key == pg.K_LEFT:
                if direcao2[0] >= 5:
                    direcao2[0] -= 5
            if event.key == pg.K_RIGHT:
                if direcao2[0] <= 255:
                    direcao2[0] += 5
            if event.key == pg.K_DOWN:
                if direcao2[1] <= 255:
                    direcao2[1] += 5
            if event.key == pg.K_UP:
                if direcao2[1] >= 5:
                    direcao2[1] -= 5


    pg.draw.rect(screen, cor3, (direcao2[0], direcao2[1], 40, 40))

    if direcao1[0] > direcao2[0]:
        pg.draw.rect(screen, cor1, (direcao1[0], direcao1[1], 40, 40))
    else:
        pg.draw.rect(screen, cor2, (direcao1[0], direcao1[1], 40, 40))

    pg.display.flip()
