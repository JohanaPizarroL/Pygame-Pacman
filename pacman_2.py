import pygame

pygame.init()

#criando uma tela
screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0) # seus valores (RGB)
PRETO = (0, 0, 0) # ausencia de cores

#criando a classe pacman
class Pacman:
    def __init__(self):

        self.coluna = 1
        self.linha = 1  # posicao inicial do pacman
        self.centro_x = 400 # meio da tela - largura
        self.centro_y = 300 # meio da tela - altura
        self.tamanho = 800 // 10
        self.raio = self.tamanho // 2 # raio = metade do tamanho do círculo
        self.vel_x = 1
        self.vel_y = 1

    def calcular_regras(self): # regras do pacman para andar
        self.coluna = self.coluna + self.vel_x # muda posicao, coluna
        self.linha = self.linha + self.vel_y   # muda posicao, linha
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

       # self.centro_x = self.centro_x + self.vel_x
       # self.centro_y = self.centro_y + self.vel_y

        # testes de colisão
        if(self.centro_x + self.raio > 800):
            self.vel_x = -1
        if(self.centro_x - self.raio < 0):
            self.vel_x = 1
        if(self.centro_y + self.raio > 600):
            self.vel_y = -1
        if(self.centro_y - self.raio < 0):
            self.vel_y = 1

    # Chamando o metodo pintar, para desenhar o pacman na tela
    def pintar(self, tela): # recebe uma surface chamada tela
        # desenhando um círculo amarelo (pacman)
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # desenho do recorte da boca -> triangulo preto
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
            # colocando esses pontos em uma lista -> pontos
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO ,pontos, 0)

        # Desenho do olho do pacman - bolinha preta
        olho_x = int(self.centro_x + self.raio / 5) # devemos ter um valor inteiro ao desenhar na tela
        olho_y = int(self.centro_y - self.raio / 1.5)
        olho_raio = int(self.raio / 8)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

if __name__ == "__main__":
    pacman = Pacman()

    while True:
        # Calular as regras
        pacman.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO) # limpa tela
        pacman.pintar(screen) # desenha o pacman na tela
        pygame.display.update() # atualiza
        pygame.time.delay(100)

        # Capturar os eventos

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()


# (self.centro_x + raio) -> fica totalmente a direita
# self.centro_x + self.raio -> pq fica mais para a direita
# self.centro_y - self.raio -> pq fica mais pra cima