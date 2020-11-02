import random
import pygame.mixer

# inicialização
pygame.init()
pygame.mixer.music.load(r'Musicas\song.wav')
pygame.mixer.music.play(-1)

# seta as imagens e o display
win = pygame.display.set_mode((500, 550))
pygame.display.set_caption("Jump Game")
mario = pygame.image.load(r'Imagens\mario.png')
plataforma = pygame.image.load(r'Imagens\plataforma.png')
escada = pygame.image.load(r'Imagens\escada.png')
peach = pygame.image.load(r'Imagens\peach.png')
dk = pygame.image.load(r'Imagens\dk.png')
barril = pygame.image.load(r'Imagens\barril.png')

# declaração das variáveis
x = 60
y = 470
yDK = 25
xPlat = [15, 15, 15, 15]
yPlat = [500, 370, 240, 110]
xEscada = [375, 20, 375]
yEscada = [380, 250, 120]
niveis = [500, 370, 240, 110]
lenPlat = 471
lenEsc = 130
width = 20
height = 30
isjump = False
posBarrilY = 0
v = 10
m = 0.4
run = True
subindo = False
nivelAtual = 0
caindo = False
menu = False
venceu = False
barris = []
perdeu = False
posDk = 200

# avisa sobre o nível de dificuldade
myfont = pygame.font.SysFont("Comic Sans MS", 15)
label = myfont.render("DIGITE A DIFICULDADE NO CONSOLE", 1, (255, 255, 255))
win.blit(label, (100, 100))
pygame.display.update()
dif = int(input('Escolha um nível de dificuldade de 1 a infinito, sendo 1 o mais difícil e 0 sem barris: '))

# loop de enquanto o jogo estiver rodando
while run:
    vaiJogar = random.randint(0, dif)  # chance de jogar o barril
    posBarrilX = random.randint(50, 450)  # posicao aleatoria para o barril
    win.fill((0, 0, 0))  # pinta de preto

    # desenha na tela tudo o que iremos utilizar
    i = 0
    for xPla in xPlat:
        yPla = yPlat[i]
        win.blit(plataforma, (xPla, yPla))
        i = i + 1
    i = 0
    for xEscad in xEscada:
        yEscad = yEscada[i]
        win.blit(escada, (xEscad, yEscad))
        i = i + 1
    win.blit(peach, (60, 75))
    win.blit(mario, (x, y))
    if vaiJogar == 1 and not venceu and not perdeu and not menu and not subindo and not caindo:
        if posDk < posBarrilX:
            posDk = posDk + 3
            win.blit(dk, (posDk, yDK))
        else:
            posDk = posDk - 3
            win.blit(dk, (posDk, yDK))
    else:
        posDk = 200
        win.blit(dk, (posDk, yDK))

    for pos in barris:
        win.blit(barril, (pos[0], pos[1]))
    # fim dos desenhos

    # verifica se o usuário fechou o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # se não estiver subindo escada, se o DK não estiver caindo, se o menu não estiver aberto e se não perdeu
    if not subindo and not caindo and not menu and not perdeu:
        if vaiJogar == 1:
            barris.append([posBarrilX, posBarrilY])  # adiciona o barril no vetor caso vaiJogar seja 1

        index = 0
        for pos in barris:
            if pos[1] < 550:
                pos[1] = pos[1] + 3
            else:
                barris.pop(index)  # remove barris que já não aparecem na tela para evitar processamento desnecessário

            if pos[0] - 15 <= x <= pos[0] + 50 and pos[1] + 45 >= y > pos[1] - 20:  # caso o mário bata no barril
                run = False
                perdeu = True

            index = index + 1

        keys = pygame.key.get_pressed()  # pega a tecla pressionada
        if keys[pygame.K_LEFT]:  # esquerda
            if x > 45:
                x = x - 2.3
        if keys[pygame.K_RIGHT]:  # direita
            if x < lenPlat - 35:
                x = x + 2.3
        if keys[pygame.K_ESCAPE]:  # esc
            menu = True

        try:
            if x <= posDk + 90 and nivelAtual == 3:  # caso o mário encoste no DK
                venceu = True  # VENCEU!
                caindo = True
                dk = pygame.image.load(r'Imagens\dkDead.png')  # muda a imagem para morte
                y = 80

            # caso tente subir a escada
            if xEscada[nivelAtual] + 15 <= x <= xEscada[nivelAtual] - 45 + lenEsc and keys[pygame.K_UP] and not isjump:
                nivelAtual = nivelAtual + 1
                subindo = True
        except:  # exceção ignorada
            None

        # se não estiver pulando, deixa pular novamente
        if not isjump:
            if keys[pygame.K_SPACE]:
                isjump = True

        # cálculos físicos para o pulo
        if isjump:
            F = (1 / 2) * m * (v ** 2)
            y -= F
            v = v - 1
            if v < 0:
                m = -0.4
            if v == -11:
                isjump = False
                v = 10
                m = 0.4
    if subindo:  # se estiver subindo a escada
        if y > niveis[nivelAtual] - 30:
            y = y - 2
        else:
            subindo = False
    if caindo:  # se DK estiver caindo
        yDK = yDK + 3
        if yDK > 550:
            run = False
    # se o menu estiver aberto, escreve o menu
    if menu:
        keys = pygame.key.get_pressed()
        win.fill((0, 0, 0))
        myfont = pygame.font.SysFont("Comic Sans MS", 15)
        label = myfont.render("Jogo inspirado em Kong - Nintendo.", 1, (255, 255, 255))
        win.blit(label, (130, 100))
        label = myfont.render("A princesa Peach foi raptada pelo grandioso Donkey Kong", 1, (255, 255, 255))
        win.blit(label, (50, 200))
        label = myfont.render("e ela conta com você e seu amigo Encanador para salvá-la!", 1, (255, 255, 255))
        win.blit(label, (50, 220))
        label = myfont.render("Como jogar:", 1, (255, 255, 255))
        win.blit(label, (210, 320))
        label = myfont.render("Utilize as setas do teclado para se movimentar e espaço para pular.", 1, (255, 255, 255))
        win.blit(label, (20, 340))

        pygame.display.update()
        if keys[pygame.K_ESCAPE]:
            menu = False

    # delay de 20 ms e update na tela
    pygame.time.delay(20)
    pygame.display.update()

# se venceu, escreve que venceu
if venceu:
    win.fill((0, 0, 0))
    myfont = pygame.font.SysFont("Comic Sans MS", 15)
    label = myfont.render("VOCÊ VENCEU! A PEACH ESTÁ SALVA", 1, (255, 255, 255))
    win.blit(label, (100, 100))
    pygame.display.update()
    pygame.time.delay(10000)
# se perdeu, escreve que perdeu
if perdeu:
    win.fill((0, 0, 0))
    myfont = pygame.font.SysFont("Comic Sans MS", 15)
    label = myfont.render("VOCÊ PERDEU! A PEACH MORREU...", 1, (255, 255, 255))
    win.blit(label, (100, 100))
    pygame.display.update()
    pygame.time.delay(10000)

# fecha o jogo
pygame.quit()
