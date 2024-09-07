import pygame

pygame.init()

#criando uma tela
screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0) # seus valores (RGB)
PRETO = (0, 0, 0) # ausencia de cores
VELOCIDADE = 1

#criando a classe pacman
class Pacman:
    def __init__(self):

        self.coluna = 1
        self.linha = 1  # posicao inicial do pacman
        self.centro_x = 400 # meio da tela - largura
        self.centro_y = 300 # meio da tela - altura
        self.tamanho = 800 // 30
        self.raio = self.tamanho // 2 # raio = metade do tamanho do círculo
        self.vel_x = 0 # iniciando parado
        self.vel_y = 0

    def calcular_regras(self): # regras do pacman para andar
        self.coluna = self.coluna + self.vel_x # muda posicao, coluna
        self.linha = self.linha + self.vel_y   # muda posicao, linha
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    # Chamando o metodo pintar, para desenhar o pacman na tela
    def desenhar_pacman(self, tela): # recebe uma surface chamada tela
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


    def processa_eventos(self, eventos):
        for e in eventos: # testando as teclas
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_UP:
                    self.vel_y = 0
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0


if __name__ == "__main__":
    pacman = Pacman()

    while True:
        # Calular as regras
        pacman.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO) # limpa tela
        pacman.desenhar_pacman(screen) # desenha o pacman na tela
        pygame.display.update() # atualiza
        pygame.time.delay(100)

        # Capturar os eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            pacman.processa_eventos(eventos)
