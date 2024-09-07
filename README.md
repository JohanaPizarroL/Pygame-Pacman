# Pacman com pygame


## Pacman - desenho
Composto de três principais formas geométricas:
- Círculo amarelo preenchido
- Triangulo preto (simula sua boca)
- Círculo preto (somula seu olho)

Usando o método **draw** conseguimos desenhar diferentes formatos na tela:

**- Círculo amarelo preenchido**
  - Constante que representa a cor: AMARELO = (255, 255, 0)
  - Espessura com valor = 0, representa o círculo "preenchido" (colorido)
```
  pygame.draw.circle(<surface>, <cor>, <ponto_central>, <raio>, <espessura>)

  pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
```

**- Triangulo preto** - usando .polygon
  - Constante que representa a cor: PRETO = (0, 0, 0)
  - Espessura com valor = 0, representa o triângulo "preenchido" (colorido)
```
  pygame.draw.polygon(<Surface>, <cor>, <lista de pontos>, <espessura>)

  # pontos sendo a lista de seus pontos em coordenadas

  pontos = [canto_boca, labio_superior, labio_inferior]
  pygame.draw.polygon(tela, PRETO ,pontos, 0)
```

**- Círculo preto preenchido** - olho do pacman
```
  pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)
```


## Pacman virado pra esquerda
* Apenas invertendo os valores de inicialização do triangulo

  
O circulo, em si não muda já que é necessário apenas as coordenadas das figuras geométricas


![image](https://github.com/user-attachments/assets/e8153b7b-7d3f-445f-88eb-0e2af17aac5f)


## Função de andar com as teclas (flechas)


```
    def processa_eventos(self, eventos):
        for e in eventos: # testando as teclas pressionadas
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
```



### EVENTOS
- Existem diversos tipos de eventos, cada um com sua própria funçao, temos:
  - QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONDOWN. MOUSEBUTTONUP, entre outros.
  - Para acessar sobre mais eventos --> [eventos em pygame](https://www.pygame.org/docs/ref/event.html)
 
Cada uma tem suas propriedades, mas usamos estas por agora:

- **KEYDOWN** - quando pressionamos uma tecla

  - **unicode:** código daquela tecla
  - **key:** número que corresponde a tecla pressionada
  - **mod:** indica se foi pressionada com mais uma tecla

- **KEYUP**- indica quando se solta uma tecla (levanta o dedo)

  - **key:** número que corresponde a tecla solta
  - **mod:** indica se estávamos segurando outra tecla junto

- **MOUSEMOTION -** movimentação do mouse
  
  - **pos:** posição atual do mouse
  - **rel:** deslocamento relativo, quanto ele se deslocou
  - **buttons:** quais botões foram usados enquanto usam o mouse
 

Devemos fazer a verificação se a tecla foi pressionada e outra se ela for solta, caso contrário ao pressionar a tecla ela vai andar "infinitamente"

  - K_RIGHT: flecha para direita
  - K_LEFT: flecha para esquerda
  - K_UP: flecha para cima
  - K_DOWN: flecha para baixo

- **TESTANDO SE KEYDOWN** - se tal tecla foi pressioanada
  ```
  if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_RIGHT: # se a tecla da flecha pra direita foi pressionada...
        self.vel_x = VELOCIDADE   # sua velocidade atual muda = 1, VELOCIDADE anda 1 espaço por vez
  
  # continúa com as outras teclas...
  ```

- **TESTANDO SE KEYUP** - se tal tecla foi solta
  ```
  elif e.type == pygame.KEYUP
      if e.key == pygame.K_RIGHT: # se a tecla da flecha pra direita foi solta...
        self.vel_x = 0            # sua velocidade atual é zerada, não anda mais
  
  # continúa com as outras teclas...
  ```

















