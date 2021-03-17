import pygame
import time
import random

pygame.init()

azul=(0,0,255)
verde=(0,255,0)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho=(255,0,0)
fonte = pygame.font.SysFont(None, 30)

larguraTela = 800
alturaTela  = 600

clock = pygame.time.Clock()

posicaoCobra=10
velocidadeCobra=30

tela=pygame.display.set_mode((larguraTela, alturaTela))

pygame.display.set_caption('Jogo da cobrinha')

def mensagem(msg,color):
    mesg = fonte.render(msg, True, color)
    tela.blit(mesg, [larguraTela/7, alturaTela/2.3])

def pontuacao(pontos):
    value = fonte.render("Pontos: " + str(pontos), True, branco)
    tela.blit(value, [0, 0])

def cobra(posicaoCobra, listaCobra):
    for x in listaCobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], posicaoCobra, posicaoCobra])

def jogo():
    fecharJogo=False
    fimDeJogo=False

    x1 = larguraTela/2
    y1 = alturaTela/2

    x1_change = 0       
    y1_change = 0

    listaCobra = []
    tamanhoCobra = 1

    comidaX = round(random.randrange(0, larguraTela - posicaoCobra) / 10.0) * 10.0
    comidaY = round(random.randrange(0, alturaTela - posicaoCobra) / 10.0) * 10.0

    while not fimDeJogo:
        while fecharJogo == True:
            tela.fill(preto)
            mensagem("Você perdeu! Pressione q para sair ou c para jogar novamente", vermelho)
            pontuacao(tamanhoCobra -1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    if event.key == pygame.K_q:
                        fimDeJogo = True
                        fecharJogo = False
                    if event.key == pygame.K_c:
                        jogo()

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
            fecharJogo = True
    
        x1 += x1_change
        y1 += y1_change
        tela.fill(preto)
        pygame.draw.rect(tela, azul, [comidaX, comidaY, posicaoCobra, posicaoCobra])
    
        cabecaCobra = []
        cabecaCobra.append(x1)
        cabecaCobra.append(y1)
        listaCobra.append(cabecaCobra)
        if len(listaCobra) > tamanhoCobra:
            del listaCobra[0]
 
        for x in listaCobra[:-1]:
            if x == cabecaCobra:
                fecharJogo = True
 
        cobra(posicaoCobra, listaCobra)
        pontuacao(tamanhoCobra -1)

        pygame.display.update()
    
        if x1 == comidaX and y1 == comidaY:
            print("Delicia")
            comidaX = round(random.randrange(0, larguraTela - posicaoCobra) / 10.0) * 10.0
            comidaY = round(random.randrange(0, alturaTela - posicaoCobra) / 10.0) * 10.0
            tamanhoCobra += 1
        clock.tick(velocidadeCobra)

    pygame.quit()
    quit()
jogo()
