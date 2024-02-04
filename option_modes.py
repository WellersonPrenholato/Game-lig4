from jogada import *
from pontuacao import *
from matriz import *
from extra import *

caracter_jogador_A = "O"
caracter_jogador_B = "X"

def modeAllPositions(): # Modo de jogo, preencher todas as posições.
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
    pt_jogador_A, list_lines_pts_A = pontuacaoVertical(matriz, caracter_jogador_A, nc, nl)
    print(f"\nPontuação na(s) linha(s): {list_lines_pts_A}. ", end='')
    print(f"\nO Jogador A ({caracter_jogador_A}) fez {pt_jogador_A} pt(s) na vertical.")
    
    pt_jogador_A, list_columns_pts_A = pontuacaoHorizontal(matriz, caracter_jogador_A, nc, nl)
    print(f"\nPontuação na(s) coluna(s): {list_columns_pts_A}. ", end='')
    print(f"\nO Jogador A ({caracter_jogador_A}) fez {pt_jogador_A} pt(s) na horizontal.")
    
    print("*" * 40)
    pt_jogador_B, list_lines_pts_B = pontuacaoVertical(matriz, caracter_jogador_B, nc, nl)
    print(f"\nPontuação na(s) linha(s): {list_lines_pts_B}. ", end='')
    print(f"\nO Jogador B ({caracter_jogador_B}) fez {pt_jogador_B} pt(s) na vertical.")
    
    pt_jogador_B,list_columns_pts_B = pontuacaoHorizontal(matriz, caracter_jogador_B, nc, nl)
    print(f"\nPontuação na(s) coluna(s): {list_columns_pts_B}. ", end='')
    print(f"\nO Jogador B ({caracter_jogador_B}) fez {pt_jogador_B} pt(s) na horizontal.")

    print()


def modeOneGold(): # Modo de jogo ponto único.
    # Constrói matriz de zeros
    matriz = [ [0 for i in range(nc)] for j in range(nl)]
    matriz = constroiMatriz(matriz, nc, nl)

    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)

    flag_pontuacao = True
    while (flag_pontuacao):
        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")

        jogador1 = int(input("Jogador 1 informe a coluna: "))
        matriz = registraJogada(matriz, jogador1, caracter_jogador_A, 1)
        print(f"O jogador 1 realizou a jogada com SUCESSO! ({caracter_jogador_A})\n")

        # PONTUAÇÃO - JOGADOR A
        pt_jogador_A_vert, _ = pontuacaoVertical(matriz, caracter_jogador_A, nc, nl)
        pt_jogador_A_horiz, _ = pontuacaoHorizontal(matriz, caracter_jogador_A, nc, nl)

        if (pt_jogador_A_vert > 0 or pt_jogador_A_horiz > 0):
            flag_pontuacao = False
            print(f"O Jogador 1 ({caracter_jogador_A}) GANHOU A PARTIDA!\n")
            print("*** JOGO FINALIZADO! ***")
            exit()

        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")
        jogador2 = int(input("Jogador 2 informe a coluna: "))
        matriz = registraJogada(matriz, jogador2, caracter_jogador_B, 2)
        print(f"O jogador 2 realizou a jogada com SUCESSO! ({caracter_jogador_B})\n")

        # PONTUAÇÃO - JOGADOR B
        pt_jogador_B_vert, _ = pontuacaoVertical(matriz, caracter_jogador_B, nc, nl)
        pt_jogador_B_horiz, _ = pontuacaoHorizontal(matriz, caracter_jogador_B, nc, nl)

        if (pt_jogador_B_vert > 0 or pt_jogador_B_horiz > 0):
            flag_pontuacao = False
            print(f"O Jogador 2 ({caracter_jogador_B}) GANHOU A PARTIDA!\n")
            print("*** JOGO FINALIZADO! ***")
            exit()
