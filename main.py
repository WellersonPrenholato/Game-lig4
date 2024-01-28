import math
from jogadas import registraJogada
from pontuacao import *

nl = 6
nc = 7

caracter_jogador_A = "O"
caracter_jogador_B = "X"

##########################################################
##########################################################

def escreveTitle():
    print("  ************************")
    print("  *****  GAME LIG 4  *****")
    print("  ************************")
    print(f"  O jogador 1 possui o caracter: {caracter_jogador_A}")
    print(f"  O jogador 2 possui o caracter: {caracter_jogador_B}")
    print()


def constroiMatriz(matriz, nc: int, nl: int):
    matriz = [['_' for _ in range(nc)] for _ in range(nl)]

    return matriz

def imprimeMatriz(matriz, nc: int, nl: int):
    indx_linha = nl
    for i in range(nl):
        print(f' | ' + ' | '.join(matriz[i]) + f' | {indx_linha}')
        indx_linha-=1

    # Imprimir rótulos das colunas
    rotulos_colunas = [str(i) for i in range(1, nc + 1, 1)]
    print(' | ' + ' | '.join(rotulos_colunas) + ' | ')


# Verificar se é possível jogar na coluna informada. Return: true, false
def verificaColuna(matriz: str, indx: int):
    if (matriz[0][(indx) - 1] != "_"): # Topo da matriz
        return False
    else:
        return True

def verificaColunaVarredura(matriz: str): #matriz[linha][coluna]
    list_column_completed = []
    for indice_col in range(nc):
        if (matriz[0][(indice_col)] != "_"): # Topo da matriz/coluna.
            list_column_completed.append(indice_col + 1)
    return list_column_completed

def diagonal_direita():
    
    return

def diagonal_esquerda():
    return

def pontuacao_geral ():
    # Contabiliza todos os pontos (ambos jogadores) e apresenta uma mensagem falando que todas as posições estão ocupadas.
    return


def mode_all_positions(): # Modo de jogo, preencher todas as posições
    # Constrói matriz de zeros
    matriz = [ [0 for i in range(nc)] for j in range(nl)]
    matriz = constroiMatriz(matriz, nc, nl)

    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)

    colunas_completas = []
    # Ainda falta corrigir quando toda matriz fica preenchida
    while (len(colunas_completas) < nc):

        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")
        # print()
        jogador1 = int(input("Jogador 1 informe a coluna: "))
        matriz = registraJogada(matriz, jogador1, caracter_jogador_A, 1)
        print(f"O jogador 1 realizou a jogada com SUCESSO! ({caracter_jogador_A})\n")
        
        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")
        # print()
        jogador2 = int(input("Jogador 2 informe a coluna: "))
        matriz = registraJogada(matriz, jogador2, caracter_jogador_B, 2)
        print(f"O jogador 2 realizou a jogada com SUCESSO! ({caracter_jogador_B})\n")
        
        colunas_completas = verificaColunaVarredura(matriz)
        # colunas_completas = list(filter(lambda x: x != '', colunas_completas))
        # print(f"Colunas completas: {list(set(colunas_completas))}")

    imprimeMatriz(matriz, nc, nl)
    # print(f"Colunas completas: {colunas_completas}\n")

    print("Não é possível realizar mais jogadas!" +
        "\n*** JOGO ENCERRADO!\n")
    
    print("*" * 40)
    pt_jogador_A = pontuacaoVertical(matriz, caracter_jogador_A, nc, nl)
    print(f"\nO Jogador A ({caracter_jogador_A}) fez {pt_jogador_A} pt(s) na vertical.")
    pt_jogador_A = pontuacaoHorizontal(matriz, caracter_jogador_A, nc, nl)
    print(f"\nO Jogador A ({caracter_jogador_A}) fez {pt_jogador_A} pt(s) na horizontal.")
    
    print("*" * 40)
    pt_jogador_B = pontuacaoVertical(matriz, caracter_jogador_B, nc, nl)
    print(f"\nO Jogador B ({caracter_jogador_B}) fez {pt_jogador_B} pt(s) na vertical.")
    pt_jogador_B = pontuacaoHorizontal(matriz, caracter_jogador_B, nc, nl)
    print(f"\nO Jogador B ({caracter_jogador_B}) fez {pt_jogador_B} pt(s) na horizontal.")

    print()


def mode_one_gold(): # Modo de jogo ponto único.
    
    print()


if __name__ == "__main__":
    
    print ("Informe o modo do jogo que deseja jogar:")
    print("1 - Preencha todas as posições. ")
    print("2 - Quem fizer o primeiro ponto ganha.")

    entrada = int(input("Informe: "))

    escreveTitle()

    if entrada == 1:
        mode_all_positions()
    elif (entrada == 2):
        mode_one_gold()
    else:
        print("O valor informado não corresponde as opções informadas.\n")
        exit()

    # print()