"""
Module for scoring in Lig4 game.
Contains functions to calculate points for horizontal, vertical, and diagonal sequences.
"""

import math

# Pontuação reta.
def pontuacaoHorizontal(matriz: list, caracter_jogador: str, nc: int, nl: int) -> tuple:
    """
    Calculate horizontal points for a player.
    
    Args:
        matriz: Game board
        caracter_jogador: Player's character ('O' or 'X')
        nc: Number of columns
        nl: Number of lines
    
    Returns:
        Tuple of (points, list of lines with points)
    """
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
def pontuacaoDiagonalEsquerda(matriz, caracter_jogador, nc, nl):
    count_pontuacao = 0
    # Verificar diagonais da esquerda para direita (crescente)
    for linha in range(nl - 3):
        for coluna in range(nc - 3):
            if (matriz[linha][coluna] == caracter_jogador and
                matriz[linha+1][coluna+1] == caracter_jogador and
                matriz[linha+2][coluna+2] == caracter_jogador and
                matriz[linha+3][coluna+3] == caracter_jogador):
                count_pontuacao += 1
    return count_pontuacao

def pontuacaoDiagonalDireita(matriz, caracter_jogador, nc, nl):
    count_pontuacao = 0
    # Verificar diagonais da direita para esquerda (decrescente)
    for linha in range(nl - 3):
        for coluna in range(3, nc):
            if (matriz[linha][coluna] == caracter_jogador and
                matriz[linha+1][coluna-1] == caracter_jogador and
                matriz[linha+2][coluna-2] == caracter_jogador and
                matriz[linha+3][coluna-3] == caracter_jogador):
                count_pontuacao += 1
    return count_pontuacao

def pontuacao_geral(matriz, caracter_jogador, nc, nl):
    pt_horiz = pontuacaoHorizontal(matriz, caracter_jogador, nc, nl)[0]
    pt_vert = pontuacaoVertical(matriz, caracter_jogador, nc, nl)[0]
    pt_diag_esq = pontuacaoDiagonalEsquerda(matriz, caracter_jogador, nc, nl)
    pt_diag_dir = pontuacaoDiagonalDireita(matriz, caracter_jogador, nc, nl)
    return pt_horiz + pt_vert + pt_diag_esq + pt_diag_dir