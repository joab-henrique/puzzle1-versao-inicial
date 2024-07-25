import pygame
from random import randint

def comecar_partida():
    print('em desenvolvimento...')

# Inicializa o Pygame:
pygame.init()

# Define a tela com o seu respectivo tamanho:
tela = pygame.display.set_mode((1280, 720))

# Define um nome pro jogo (aparece no canto superior da tela):
pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')

# Variáveis para carregar a cena inicial da fase:
cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena1.png')  # Coleta a cena inicial
cena = pygame.transform.scale(cena, (1280, 720))  # Ajusta a imagem para cobrir a tela inteira
aux_cena = 1  # Variável auxiliar para determinar qual a cena que está sendo exibida

# Seta a visualização da tela como sendo a imagem da cena:
tela.blit(cena, (0, 0))

# Atualiza o display inicial do jogo:
pygame.display.flip()

# Criação de variáveis do placar da partida:
pontos_robocin = 0
pontos_voxar = 0

# ----- Declarações de funções: -----

# Função para desenhar um botão:
def desenhar_botao(cena, cor, posicao_x, posicao_y, largura, altura, texto):
    pygame.draw.rect(cena, cor, (posicao_x, posicao_y, largura, altura)) #Desenha um retângulo
    font = pygame.font.Font(None, 36) #Determina uma fonte
    texto_superficie = font.render(texto, True, (0, 0, 0)) #Coleta um texto pra ficar na superfície da tela
    text_rect = texto_superficie.get_rect(center = (posicao_x + largura // 2, posicao_y + altura // 2)) #Coleta o texto do retângulo
    cena.blit(texto_superficie, text_rect) #Exibe os textos na cena

# Função para alterar a cena de acordo com a cena atual:
def alterar_cena():
    global aux_cena # Chama a variável global da cena auxiliar

    # Se a cena atual for a 1, então carrega o segundo cenário e assim sucessivamente:
    if aux_cena == 1:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena2.png')
    elif aux_cena == 2:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena3.png')
    elif aux_cena == 3:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena4.png')
    elif aux_cena == 4:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena5.png')
    elif aux_cena == 5:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena6.png')
    elif aux_cena == 6:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena7.png')
    elif aux_cena == 7:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena8.png')
    elif aux_cena == 8:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena9.png')
    elif aux_cena == 9:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena10.png')
    elif aux_cena == 10:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena11.png')
    elif aux_cena == 11:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena12.png')
    elif aux_cena == 12:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena13.png')
    # Se a cena for a última da introdução, então começa a partida:
    elif aux_cena == 13:
        partida_chute()

    cena = pygame.transform.scale(cena, (1280, 720))
    tela.blit(cena, (0, 0))
    pygame.display.flip()
    aux_cena += 1

# Função para chutar na partida (disputa de penâltis):
def partida_chute():
    cena = pygame.image.load('imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCINvsVOXAR.png')
    cena = pygame.transform.scale(cena, (1280, 720))
    tela.blit(cena, (0, 0))
    pygame.display.flip()

    # Cria os botões de seleção:
    botao_esquerda = pygame.Rect(200, 600, 200, 50)
    botao_centro = pygame.Rect(500, 600, 200, 50)
    botao_direita = pygame.Rect(800, 600, 200, 50)

    # Variável para definir se a partida está sendo acontecendo (se True). Se False, é devido ao jogador ter terminado:
    status_partida = True

    # Executa um loop infinito para executar a partida:
    while status_partida:

        # Executa um loop percorrendo as ações realizadas no jogo:
        for event in pygame.event.get():
            # Se a ação realizada for clicar no botão de fechar a tela, sai do jogo:
            if event.type == pygame.QUIT:
                status_partida = False

            # Se a ação realizada for clicar em um botão do mouse:
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos #Coleta o clique

                # Realiza uma ação de acordo com o botão pressionado:
                if botao_esquerda.collidepoint(mouse_x, mouse_y):
                    # Se os pontos somados não for igual a 10 (cada equipe jogou 5 rodadas).
                    if pontos_robocin + pontos_voxar != 10:
                        print('em desenvolvimento...')
                    else:
                        print('em desenvolvimento...')

                elif botao_centro.collidepoint(mouse_x, mouse_y):
                    if pontos_robocin + pontos_voxar != 10:
                        print('em desenvolvimento...')
                    else:
                        print('em desenvolvimento...')

                elif botao_direita.collidepoint(mouse_x, mouse_y):
                    if pontos_robocin + pontos_voxar != 10:
                        print('em desenvolvimento...')
                    else:
                        print('em desenvolvimento...')

        #Desenha os botões e exibe na tela:
        tela.blit(cena, (0, 0))
        desenhar_botao(tela, (51, 255, 255), botao_esquerda.x, botao_esquerda.y, botao_esquerda.width, botao_esquerda.height, 'Esquerda')
        desenhar_botao(tela, (51, 255, 255), botao_centro.x, botao_centro.y, botao_centro.width, botao_centro.height, 'Centro')
        desenhar_botao(tela, (51, 255, 255), botao_direita.x, botao_direita.y, botao_direita.width, botao_direita.height, 'Direita')
        pygame.display.flip()

# ----- Execução do jogo: -----

#Variável para definir se o jogo está sendo executado (se True). Se False, é devido ao jogador ter fechado a tela:
status_jogo = True

#Executa um loop infinito para rodar o jogo:
while status_jogo:

    # Executa um loop percorrendo as ações realizadas no jogo:
    for event in pygame.event.get():
        # Se a ação realizada for clicar no botão de fechar a tela, sai do jogo:
        if event.type == pygame.QUIT:
            status_jogo = False
        # Se ação realizada for clicar em uma tecla:
        elif event.type == pygame.KEYDOWN:
            # Se a tecla for o ENTER, chama a função de alterar a cena do jogo:
            if event.key == pygame.K_RETURN:
                alterar_cena()