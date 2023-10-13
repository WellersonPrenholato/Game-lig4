import math

def escreveTitle():
    print("  **************************")
    print("  *****   GAME LIG 4   *****")
    print("  **************************")
    print()


def main():
    nlinhas = 6
    ncolunas = 6
    escreveTitle()
    
    # matriz = [ [0 for i in range(ncolunas)] for j in range(nlinhas)]
    
    matriz = constroiMatriz(nlinhas, ncolunas)
    
    caracter_jogador_A = "O"
    # JOGADAS
    # matriz = registraJogada(matriz, 1, caracter_jogador_A)
    
    
def constroiMatriz(ncolunas, nlinhas):
    # Inicialização da matriz
    matriz = [['_' for _ in range(ncolunas)] for _ in range(nlinhas)]

    # Preencher os rótulos das colunas
    rotulos_colunas = ['1', '2', '3', '4', '5', '6', '7']

    # Preencher os rótulos das linhas à direita
    rotulos_linhas = ['a', 'd', 'c', 'd', 'e', 'f']

    # Preencher a matriz com os valores desejados
    # for i in range(linhas):
    #     for j in range(colunas):
    #         matriz[i][j] = rotulos_linhas[i] if j == 0 or j == 6 else '_'
    
    return matriz


    imprimeMatriz(matriz, nlinhas, rotulos_linhas)

    # Imprimir rótulos das colunas
    print(' | ' + ' | '.join(rotulos_colunas) + ' | ')


def registraJogada(matriz, indice_jogada: int, caracter: str):
    
    # col = (2 * indice_jogada) - 1 
    
    # if (matriz[0][col] != "_"):
    #     if (col == 1):
    #         coluna_jogada = 1
    #     else:
    #         coluna_jogada = abs(math.ceil(col/2))
            
    #     print(f"Não é possível jogar na coluna {coluna_jogada}!")
    #     print()
        
    # for i in range(5, -1, -1):
    #     if (matriz[i][col] == "_"):
    #         matriz[i][col] = caracter
    #         break
    #     if (matriz[i][col] != "_"):
    #         continue
    
    return matriz



def imprimeMatriz(matriz, nl: int, rotulos_linhas): 
    # Imprimir a matriz
    for i in range(nl):
        print(' | ' + ' | '.join(matriz[i]) + f' | {rotulos_linhas[i]}' + ' | ')


# Chamada da função main
if __name__ == "__main__":
    main()