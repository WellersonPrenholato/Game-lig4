from jogada import *
from pontuacao import *
from matriz import *
from extra import *

caracter_jogador_A = "O"
caracter_jogador_B = "X"

def modeAllPositions(): # Modo de jogo, preencher todas as posições.
    # Constrói matriz
    matriz = constroiMatriz([], nc, nl)

    while True:
        if verificaTabuleiroCheio(matriz, nc):
            break

        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")
        try:
            jogador1 = int(input("Jogador 1 informe a coluna: "))
        except ValueError:
            print("Entrada inválida. Informe um número entre 1 e 7.")
            continue
        matriz = registraJogada(matriz, jogador1, caracter_jogador_A, 1)
        print(f"O jogador 1 realizou a jogada com SUCESSO! ({caracter_jogador_A})\n")
        
        if verificaTabuleiroCheio(matriz, nc):
            break

        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")
        try:
            jogador2 = int(input("Jogador 2 informe a coluna: "))
        except ValueError:
            print("Entrada inválida. Informe um número entre 1 e 7.")
            continue
        matriz = registraJogada(matriz, jogador2, caracter_jogador_B, 2)
        print(f"O jogador 2 realizou a jogada com SUCESSO! ({caracter_jogador_B})\n")

    imprimeMatriz(matriz, nc, nl)
    # print(f"Colunas completas: {colunas_completas}\n")

    print("Não é possível realizar mais jogadas!" +
        "\n*** JOGO ENCERRADO!\n")
    
    print("*" * 40)
    pt_vert_A, list_lines_pts_A = pontuacaoVertical(matriz, caracter_jogador_A, nc, nl)
    print(f"\nPontuação na(s) linha(s): {list_lines_pts_A}. ", end='')
    print(f"\nO Jogador A ({caracter_jogador_A}) fez {pt_vert_A} pt(s) na vertical.")
    
    pt_horiz_A, list_columns_pts_A = pontuacaoHorizontal(matriz, caracter_jogador_A, nc, nl)
    print(f"\nPontuação na(s) coluna(s): {list_columns_pts_A}. ", end='')
    print(f"\nO Jogador A ({caracter_jogador_A}) fez {pt_horiz_A} pt(s) na horizontal.")
    
    pt_diag_esq_A = pontuacaoDiagonalEsquerda(matriz, caracter_jogador_A, nc, nl)
    pt_diag_dir_A = pontuacaoDiagonalDireita(matriz, caracter_jogador_A, nc, nl)
    print(f"\nO Jogador A ({caracter_jogador_A}) fez {pt_diag_esq_A} pt(s) na diagonal esquerda e {pt_diag_dir_A} pt(s) na diagonal direita.")
    
    print("*" * 40)
    pt_vert_B, list_lines_pts_B = pontuacaoVertical(matriz, caracter_jogador_B, nc, nl)
    print(f"\nPontuação na(s) linha(s): {list_lines_pts_B}. ", end='')
    print(f"\nO Jogador B ({caracter_jogador_B}) fez {pt_vert_B} pt(s) na vertical.")
    
    pt_horiz_B, list_columns_pts_B = pontuacaoHorizontal(matriz, caracter_jogador_B, nc, nl)
    print(f"\nPontuação na(s) coluna(s): {list_columns_pts_B}. ", end='')
    print(f"\nO Jogador B ({caracter_jogador_B}) fez {pt_horiz_B} pt(s) na horizontal.")
    
    pt_diag_esq_B = pontuacaoDiagonalEsquerda(matriz, caracter_jogador_B, nc, nl)
    pt_diag_dir_B = pontuacaoDiagonalDireita(matriz, caracter_jogador_B, nc, nl)
    print(f"\nO Jogador B ({caracter_jogador_B}) fez {pt_diag_esq_B} pt(s) na diagonal esquerda e {pt_diag_dir_B} pt(s) na diagonal direita.")

    total_A = pt_vert_A + pt_horiz_A + pt_diag_esq_A + pt_diag_dir_A
    total_B = pt_vert_B + pt_horiz_B + pt_diag_esq_B + pt_diag_dir_B

    print(f"\nTotal Jogador A: {total_A} pontos")
    print(f"Total Jogador B: {total_B} pontos")

    if total_A > total_B:
        print("Jogador A venceu!")
    elif total_B > total_A:
        print("Jogador B venceu!")
    else:
        print("Empate!")

    print()


def modeOneGold(): # Modo de jogo ponto único.
    # Constrói matriz
    matriz = constroiMatriz([], nc, nl)

    flag_pontuacao = True
    while (flag_pontuacao):
        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")

        try:
            jogador1 = int(input("Jogador 1 informe a coluna: "))
        except ValueError:
            print("Entrada inválida. Informe um número entre 1 e 7.")
            continue
        matriz = registraJogada(matriz, jogador1, caracter_jogador_A, 1)
        print(f"O jogador 1 realizou a jogada com SUCESSO! ({caracter_jogador_A})\n")

        # PONTUAÇÃO - JOGADOR A
        pt_jogador_A_vert, _ = pontuacaoVertical(matriz, caracter_jogador_A, nc, nl)
        pt_jogador_A_horiz, _ = pontuacaoHorizontal(matriz, caracter_jogador_A, nc, nl)
        pt_jogador_A_diag_esq = pontuacaoDiagonalEsquerda(matriz, caracter_jogador_A, nc, nl)
        pt_jogador_A_diag_dir = pontuacaoDiagonalDireita(matriz, caracter_jogador_A, nc, nl)

        if (pt_jogador_A_vert > 0 or pt_jogador_A_horiz > 0 or pt_jogador_A_diag_esq > 0 or pt_jogador_A_diag_dir > 0):
            flag_pontuacao = False
            print(f"O Jogador 1 ({caracter_jogador_A}) GANHOU A PARTIDA!\n")
            print("*** JOGO FINALIZADO! ***")
            exit()

        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")
        try:
            jogador2 = int(input("Jogador 2 informe a coluna: "))
        except ValueError:
            print("Entrada inválida. Informe um número entre 1 e 7.")
            continue
        matriz = registraJogada(matriz, jogador2, caracter_jogador_B, 2)
        print(f"O jogador 2 realizou a jogada com SUCESSO! ({caracter_jogador_B})\n")

        # PONTUAÇÃO - JOGADOR B
        pt_jogador_B_vert, _ = pontuacaoVertical(matriz, caracter_jogador_B, nc, nl)
        pt_jogador_B_horiz, _ = pontuacaoHorizontal(matriz, caracter_jogador_B, nc, nl)
        pt_jogador_B_diag_esq = pontuacaoDiagonalEsquerda(matriz, caracter_jogador_B, nc, nl)
        pt_jogador_B_diag_dir = pontuacaoDiagonalDireita(matriz, caracter_jogador_B, nc, nl)

        if (pt_jogador_B_vert > 0 or pt_jogador_B_horiz > 0 or pt_jogador_B_diag_esq > 0 or pt_jogador_B_diag_dir > 0):
            flag_pontuacao = False
            print(f"O Jogador 2 ({caracter_jogador_B}) GANHOU A PARTIDA!\n")
            print("*** JOGO FINALIZADO! ***")
            exit()

        # Verificar se o tabuleiro está cheio (empate)
        if verificaTabuleiroCheio(matriz, nc):
            flag_pontuacao = False
            print("O tabuleiro está cheio! Empate!\n")
            print("*** JOGO FINALIZADO! ***")
            exit()
