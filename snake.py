import pygame
pygame.init()
tela=pygame.display.set_mode((800,600))

pygame.display.set_caption('Jogo da cobrinha')

azul=(0,0,255)
verde=(0,255,0)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho=(255,0,0)

fimDeJogo=False

x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()

while not fimDeJogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fimDeJogo = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 += x1_change
    y1 += y1_change
    tela.fill(preto)
    pygame.draw.rect(tela, verde, [x1, y1, 10, 10])
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()
