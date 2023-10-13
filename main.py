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

def registraJogada(matriz, indice_jogada: int, caracter: str):
    col = (indice_jogada) - 1
    
    if (matriz[0][col] != "_"):
        if (col == 1):
            coluna_jogada = 1
        else:
            coluna_jogada = abs(math.ceil(col)) + 1
            
        print(f"Não é possível jogar na coluna {coluna_jogada}!")
        print()
        
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


def diagonal_direita():
    
    return

def diagonal_esquerda():
    return

def pontuacao_geral ():
    # Contabiliza todos os pontos (ambos jogadores) e apresenta uma mensagem falando que todas as posições estão ocupadas.
    return
    
def main():
    escreveTitle()
    
    # Constrói matriz de zeros
    matriz = [ [0 for i in range(nc)] for j in range(nl)]
    matriz = constroiMatriz(matriz, nc, nl)

    matriz = registraJogada(matriz, 1, caracter_jogador_A)
    matriz = registraJogada(matriz, 1, caracter_jogador_A)
    matriz = registraJogada(matriz, 1, caracter_jogador_A)
    matriz = registraJogada(matriz, 1, caracter_jogador_A)
    matriz = registraJogada(matriz, 1, caracter_jogador_A)
    matriz = registraJogada(matriz, 1, caracter_jogador_A)
    matriz = registraJogada(matriz, 1, caracter_jogador_A)

    matriz = registraJogada(matriz, 2, caracter_jogador_A)
    # matriz = registraJogada(matriz, 2, caracter_jogador_A)
    # matriz = registraJogada(matriz, 2, caracter_jogador_A)

    matriz = registraJogada(matriz, 3, caracter_jogador_A)
    matriz = registraJogada(matriz, 3, caracter_jogador_A)
    matriz = registraJogada(matriz, 3, caracter_jogador_A)
    matriz = registraJogada(matriz, 3, caracter_jogador_A)
    # matriz = registraJogada(matriz, 3, caracter_jogador_A)

    matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    # matriz = registraJogada(matriz, 4, caracter_jogador_A)
    
    matriz = registraJogada(matriz, 5, caracter_jogador_A)
    # matriz = registraJogada(matriz, 5, caracter_jogador_A)
    # matriz = registraJogada(matriz, 5, caracter_jogador_A)
    # matriz = registraJogada(matriz, 5, caracter_jogador_A)

    matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    # matriz = registraJogada(matriz, 6, caracter_jogador_A)
    
    matriz = registraJogada(matriz, 7, caracter_jogador_A)
    matriz = registraJogada(matriz, 7, caracter_jogador_A)
    matriz = registraJogada(matriz, 7, caracter_jogador_A)
    matriz = registraJogada(matriz, 7, caracter_jogador_A)
    matriz = registraJogada(matriz, 7, caracter_jogador_A)
    matriz = registraJogada(matriz, 7, caracter_jogador_A)
    matriz = registraJogada(matriz, 7, caracter_jogador_A)
    matriz = registraJogada(matriz, 7, caracter_jogador_A)

    imprimeMatriz(matriz, nc, nl)
    pt_jogador_A = pontuacaoVertical(matriz, caracter_jogador_A, nc, nl)
    print(f"\nO Jogador A fez {pt_jogador_A} pt(s) na vertical.")
    
    pt_jogador_A = pontuacaoHorizontal(matriz, caracter_jogador_A, nc, nl)
    print(f"\nO Jogador A fez {pt_jogador_A} pt(s) na horizontal.")

    print()

# Chamada da função main
if __name__ == "__main__":
    main()