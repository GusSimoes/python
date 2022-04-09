#pip install pygame

import pygame
import math

#Constantes
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
LARANJA = (255, 165, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
PI = math.pi

pygame.init()


#cria a tela gráfica
tela = pygame.display.set_mode((1200, 680), 0)
pygame.display.set_caption('Título da Janela')

#Pinta a tela
tela.fill(BRANCO)

pygame.draw.circle(tela, VERMELHO, (50,50), 10, 0)
pygame.draw.circle(tela, VERDE, (100,50), 15, 1)
pygame.draw.circle(tela, AZUL, (150,50), 20, 3)


pygame.draw.rect(tela, PRETO, pygame.Rect(200, 30, 60, 30), 0)
pygame.draw.rect(tela, PRETO, pygame.Rect(280, 30, 60, 30), 1)

pygame.draw.line(tela, VERMELHO, [450, 20], [550,130], 5)

pontos = [(50,150), (100,120), (160,140), (110, 250)]
pygame.draw.polygon(tela, AMARELO, pontos, 0)
pygame.draw.polygon(tela, VERMELHO, pontos, 1)
                                #retangulo      ang inicial, final, espessura
pygame.draw.arc(tela, VERMELHO, [250,100, 250,200], PI/2, PI, 2)
pygame.draw.arc(tela, PRETO, [250,100, 250,200], 0, PI/2, 2)
pygame.draw.arc(tela, AZUL, [250,100, 250,200], 3*PI/2,2*PI, 2)
pygame.draw.arc(tela, AMARELO, [250,100, 250,200], PI,3*PI/2, 2)

texto= "Score: {}".format(1000)
fonte = pygame.font.SysFont("arial", 48, True, False)
img_texto = fonte.render(texto, True, VERMELHO)
tela.blit(img_texto, (50,350))


pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()