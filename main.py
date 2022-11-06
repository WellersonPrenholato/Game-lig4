import math

nl = 7
nc = 15

matriz = [ [0 for i in range(nc)] for j in range(nl)]

def escreveTitle():
    print("**************************")
    print("*****   GAME LIG 4   *****")
    print("**************************")
    print()

def constroiMatriz(matriz):
    index_col = 0 

    for linha in range(nl):
        for coluna in range(nc):
            if (coluna % 2 == 0):
                matriz[linha][coluna] = "|"
            else:
                matriz[linha][coluna] = "_"
        
                if (linha == 6): # Escreve a numeração de cada coluna na última linha
                    index_col = index_col + 1
                    matriz[linha][coluna] = index_col
    return matriz           
                    
def imprimeMatriz(matriz): 
    for linha in range(nl):
        for coluna in range(nc):
            print("%2s" % matriz[linha][coluna], end='')
        print()


def registraJogada(indice_jogada: int, caracter: str):
    
    col = (2 * indice_jogada) - 1 
    
    if (matriz[0][col] != "_"):
        if (col == 1):
            coluna_jogada = 1
        else:
            coluna_jogada = abs(math.ceil(col/2))
            
        print(f"Não é possível jogar na coluna {coluna_jogada}!")
        print()
        
    for i in range(5, -1, -1):
        if (matriz[i][col] == "_"):
            matriz[i][col] = caracter
            break
        if (matriz[i][col] != "_"):
            continue
    
    return matriz

# def pontuacaoHorizontal(matriz: str, caracter_jogador: str):
#     count_pontuacao = 0
    
#     for i in range(nl):
#         for j in range(nc):
#             if (j % 2 != 0):
#                 print(f"Item: {matriz[i][j]}")
#             # if(caracter_jogador == matriz[i][j]):
#             #     count_pontuacao += 1
                
                
#     return count_pontuacao

def pontuacaoVertical(matriz: str, caracter_jogador: str):
    count_pontuacao = 0
    count_4 = 0
    list_columns_pts = []
    
    for coluna in range(nc):
        count_4 = 0
        for linha in range(nl):
            if (coluna % 2 != 0):
                
                if(caracter_jogador == matriz[linha][coluna]):
                    count_4 += 1
                    if (count_4 == 4):
                        count_pontuacao += 1
                        indice_col = abs(math.ceil(coluna/2))
                        list_columns_pts.append(indice_col)
                else:
                    count_4 = 0
                        
    print(f"\nPontuação na(s) coluna(s): {list_columns_pts}. ", end='')
                
    return count_pontuacao
    
        
caracter_jogador_A = "a"

escreveTitle()
matriz = constroiMatriz(matriz)

matriz = registraJogada(1, caracter_jogador_A)
matriz = registraJogada(1, caracter_jogador_A)
matriz = registraJogada(1, caracter_jogador_A)
matriz = registraJogada(1, caracter_jogador_A)
matriz = registraJogada(1, caracter_jogador_A)
matriz = registraJogada(1, caracter_jogador_A)

matriz = registraJogada(3, caracter_jogador_A)
matriz = registraJogada(3, caracter_jogador_A)
matriz = registraJogada(3, caracter_jogador_A)
matriz = registraJogada(3, caracter_jogador_A)
matriz = registraJogada(3, caracter_jogador_A)

matriz = registraJogada(4, caracter_jogador_A)
matriz = registraJogada(4, caracter_jogador_A)
matriz = registraJogada(4, caracter_jogador_A)
matriz = registraJogada(4, caracter_jogador_A)
matriz = registraJogada(4, caracter_jogador_A)
matriz = registraJogada(4, caracter_jogador_A)

matriz = registraJogada(6, caracter_jogador_A)
matriz = registraJogada(6, caracter_jogador_A)
matriz = registraJogada(6, caracter_jogador_A)
matriz = registraJogada(6, caracter_jogador_A)
matriz = registraJogada(6, caracter_jogador_A)
matriz = registraJogada(6, caracter_jogador_A)


imprimeMatriz(matriz)
pt_jogador_A = pontuacaoVertical(matriz, caracter_jogador_A)
print(f"O Jogador A fez {pt_jogador_A} pts na vertical.")

print()