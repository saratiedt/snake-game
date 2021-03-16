import pygame
import time
import random

pygame.init()

azul=(0,0,255)
verde=(0,255,0)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho=(255,0,0)

larguraTela = 800
alturaTela  = 600

tela=pygame.display.set_mode((larguraTela, alturaTela))

pygame.display.set_caption('Jogo da cobrinha')



fimDeJogo=False

x1 = larguraTela/2
y1 = alturaTela/2

posicaoCobra=10
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
velocidadeCobra=30

fonte = pygame.font.SysFont(None, 50)

def mensagem(msg,color):
    mesg = fonte.render(msg, True, color)
    tela.blit(mesg, [larguraTela/3, alturaTela/2.3])

while not fimDeJogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fimDeJogo = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -posicaoCobra
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = posicaoCobra
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -posicaoCobra
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = posicaoCobra
                x1_change = 0

                 
    if x1 >= larguraTela or x1 < 0 or y1 >= alturaTela or y1 < 0:
        fimDeJogo = True
 
    x1 += x1_change
    y1 += y1_change
    tela.fill(preto)
    pygame.draw.rect(tela, verde, [x1, y1, posicaoCobra, posicaoCobra])
 
    pygame.display.update()
 
    clock.tick(velocidadeCobra)
 
mensagem("Você perdeu :(",vermelho)
pygame.display.update()
time.sleep(5) 

pygame.quit()
quit()
