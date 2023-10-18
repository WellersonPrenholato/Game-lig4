import math

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
    rotulos_colunas = ['1', '2', '3', '4', '5', '6', '7']
    print(' | ' + ' | '.join(rotulos_colunas) + ' | ')

def registraJogada(matriz, indice_jogada: int, caracter: str, num_jogador: int):
    
    # Ainda falta tratar indices inexistentes na matriz. Ex: 8+
    col = (indice_jogada) - 1
    
    while (matriz[0][col] != "_"):
        if (col == 1):
            coluna_jogada = 1
        else:
            coluna_jogada = abs(math.ceil(col)) + 1
            
        print(f"*** Não é possível jogar na coluna {coluna_jogada}!")
        nova_jogada = int(input(f"\nJogador {num_jogador} jogue novamente: "))
        col = (nova_jogada) - 1
        
        # print()
        
    for i in range(nl-1, -1, -1):
        if (matriz[i][col] == "_"):
            matriz[i][col] = caracter
            break
        if (matriz[i][col] != "_"):
            continue
    
    return matriz

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
                        
    print(f"\nPontuação na(s) linha(s): {list_lines_pts}. ", end='')

    return count_pontuacao

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
                        
    print(f"\nPontuação na(s) coluna(s): {list_columns_pts}. ", end='')
                
    return count_pontuacao

# Verificar se é possível jogar na coluna informada. Return: true, false
def verificaColuna(matriz: str, indx: int):
    if (matriz[0][(indx) - 1] != "_"): # Topo da matriz
        return False
    else:
        return True
    


def diagonal_direita():
    
    return

def diagonal_esquerda():
    return

def pontuacao_geral ():
    # Contabiliza todos os pontos (ambos jogadores) e apresenta uma mensagem falando que todas as posições estão ocupadas.
    return
    
# def main():
    # escreveTitle()
    
    # # Constrói matriz de zeros
    # matriz = [ [0 for i in range(nc)] for j in range(nl)]
    # matriz = constroiMatriz(matriz, nc, nl)
    
    # # Jogar até preencher todas as posições.
    # # Jogar até alguém fazer o primeiro ponto

    # matriz = registraJogada(matriz, 1, caracter_jogador_A)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A)
    # matriz = registraJogada(matriz, 1, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 1, caracter_jogador_A)

    # matriz = registraJogada(matriz, 2, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 2, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 2, caracter_jogador_A)

    # matriz = registraJogada(matriz, 3, caracter_jogador_A)
    # matriz = registraJogada(matriz, 3, caracter_jogador_A)
    # matriz = registraJogada(matriz, 3, caracter_jogador_A)
    # matriz = registraJogada(matriz, 3, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 3, caracter_jogador_A)

    # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    
    # matriz = registraJogada(matriz, 5, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 5, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 5, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 5, caracter_jogador_A)

    # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    
    # matriz = registraJogada(matriz, 7, caracter_jogador_A)
    # matriz = registraJogada(matriz, 7, caracter_jogador_A)
    # matriz = registraJogada(matriz, 7, caracter_jogador_A)
    # matriz = registraJogada(matriz, 7, caracter_jogador_A)
    # matriz = registraJogada(matriz, 7, caracter_jogador_A)
    # matriz = registraJogada(matriz, 7, caracter_jogador_A)
    # matriz = registraJogada(matriz, 7, caracter_jogador_A)
    # # matriz = registraJogada(matriz, 7, caracter_jogador_A)

    # imprimeMatriz(matriz, nc, nl)
    # pt_jogador_A = pontuacaoVertical(matriz, caracter_jogador_A, nc, nl)
    # print(f"\nO Jogador A fez {pt_jogador_A} pt(s) na vertical.")
    
    # pt_jogador_A = pontuacaoHorizontal(matriz, caracter_jogador_A, nc, nl)
    # print(f"\nO Jogador A fez {pt_jogador_A} pt(s) na horizontal.")
    
    # verificaColuna(matriz, 1)

    # print()
    
def mode_all_positions():
    # Constrói matriz de zeros
    matriz = [ [0 for i in range(nc)] for j in range(nl)]
    matriz = constroiMatriz(matriz, nc, nl)
    
    # Jogar até preencher todas as posições.
    
    matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)
    matriz = registraJogada(matriz, 1, caracter_jogador_A, 1)

    coluna_completa = []
    for idx_col in range(nl):
        if (verificaColuna(matriz, idx_col) == False):
            coluna_completa.append(idx_col)
            
    while (len(coluna_completa) < nc):
        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")
        # print()
        jogador1 = int(input("Jogador 1 informe a coluna: "))
        matriz = registraJogada(matriz, jogador1, caracter_jogador_A, 1)
        print("O jogador 1 realizou a jogada com SUCESSO!\n")
        
        imprimeMatriz(matriz, nc, nl)
        print("--------------------------------")
        # print()
        jogador2 = int(input("Jogador 2 informe a coluna: "))
        matriz = registraJogada(matriz, jogador2, caracter_jogador_B, 2)
        print("O jogador 2 realizou a jogada com SUCESSO!\n")

    imprimeMatriz(matriz, nc, nl)
    print(f"Colunas completas: {coluna_completa}\n")

    print("Não é possível realizar mais jogadas!" +
        "\n*** JOGO ENCERRADO!\n")
    
    pt_jogador_A = pontuacaoVertical(matriz, caracter_jogador_A, nc, nl)
    print(f"\nO Jogador A fez {pt_jogador_A} pt(s) na vertical.")
    
    pt_jogador_A = pontuacaoHorizontal(matriz, caracter_jogador_A, nc, nl)
    print(f"\nO Jogador A fez {pt_jogador_A} pt(s) na horizontal.")

    print()

def mode_one_gold():
    
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
    
    # main()