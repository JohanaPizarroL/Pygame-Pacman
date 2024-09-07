import pygame

pygame.init()

#criando uma tela
screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0) # seus valores (RGB)
PRETO = (0, 0, 0) # ausencia de cores

#criando a classe
class Pacman:
    def __init__(self):
        self.centro_x = 400 # meio da tela - largura
        self.centro_y = 300 # meio da tela - altura
        self.tamanho = 100 #pixels
        self.raio = int(self.tamanho / 2) # raio = metade do tamanho do círculo

    # chamando o metodo pintar, para desenhar o pacman na tela
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
        # Pintar a tela
        pacman.pintar(screen)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()


# (self.centro_x + raio) -> fica totalmente a direita
# self.centro_x + self.raio -> pq fica mais para a direita
# self.centro_y - self.raio -> pq fica mais pra cima