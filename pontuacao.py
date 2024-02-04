import math

# Pontuação reta.
def pontuacaoHorizontal(matriz: str, caracter_jogador: str, nc: int, nl: int):
    count_pontuacao = 0
    count_4 = 0
    list_lines_pts = []
    
    for linha in range(nl):
        count_4 = 0
        for coluna in range(nc):
            if(caracter_jogador == matriz[linha][coluna]):
                count_4 += 1
                if (count_4 == 4):
                    count_pontuacao += 1
                    indice_line = abs(math.ceil(linha))
                    list_lines_pts.append(nl - indice_line)
                    list_lines_pts.sort()
            else:
                count_4 = 0
    return count_pontuacao, list_lines_pts

def pontuacaoVertical(matriz: str, caracter_jogador: str, nc: int, nl: int):
    count_pontuacao = 0
    count_4 = 0
    list_columns_pts = []
    
    for coluna in range(nc):
        count_4 = 0
        for linha in range(nl):
            if(caracter_jogador == matriz[linha][coluna]):
                count_4 += 1
                if (count_4 == 4):
                    count_pontuacao += 1
                    indice_col = abs(math.ceil(coluna))
                    list_columns_pts.append(indice_col + 1)
            else:
                count_4 = 0
    return count_pontuacao, list_columns_pts

# Pontuação diagonal.
def diagonal_direita():
    return

def diagonal_esquerda():
    return

def pontuacao_geral ():
    # Contabiliza todos os pontos (ambos jogadores) e apresenta uma mensagem falando que todas as posições estão ocupadas.
    return