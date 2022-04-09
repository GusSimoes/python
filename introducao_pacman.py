#constantes
LARGURA = 500
ALTURA = 680
TELA = (LARGURA, ALTURA)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 0.1
RAIO = 30

import pygame

#Cria a tela gráfica
tela = pygame.display.set_mode(TELA, 0)
pygame.display.set_caption('Game com Python')

x=100
y=100
vel_x = VELOCIDADE
vel_y = VELOCIDADE


#loop do jogo
while True:

    #Calcula regras do game
    x += vel_x
    y += vel_y

    if x + RAIO > LARGURA:
        vel_x = -VELOCIDADE
    elif x - RAIO < 0:
        vel_x = VELOCIDADE

    if y + RAIO > ALTURA:
        vel_y = -VELOCIDADE
    elif y - RAIO < 0:
        vel_y = VELOCIDADE

    #Pinta a tela
    tela.fill(PRETO)
    local = x,y
    pygame.draw.circle(tela, AMARELO, local, RAIO, 0)
    pygame.display.update()

    #Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()



