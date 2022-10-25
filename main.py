nl = 7
nc = 13

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
        
                if (linha == 6):
                    index_col = index_col + 1
                    matriz[linha][coluna] = index_col
    return matriz           
                    
def imprimeMatriz(matriz): 
    for linha in range(nl):
        for coluna in range(nc):
            print("%2s" % matriz[linha][coluna], end='')
        print()


def jogada(col: int, caracter: str):
    if (matriz[0][col] != "_"):
        print(f"Não é possível jogar na coluna {col}!")
        print()
        
    for i in range(5, -1, -1):
        # print(f"LINHA:{i}")
        if (matriz[i][col] == "_"):
            matriz[i][col] = caracter
            break
        if (matriz[i][col] != "_"):
            continue
    
    return matriz
        

escreveTitle()
matriz = constroiMatriz(matriz)
matriz = jogada(1, "a")
matriz = jogada(1, "a")
matriz = jogada(1, "a")
matriz = jogada(1, "a")
matriz = jogada(1, "b")
matriz = jogada(1, "b")
matriz = jogada(1, "b")
matriz = jogada(3, "c")
matriz = jogada(3, "c")
matriz = jogada(3, "c")
matriz = jogada(3, "c")
matriz = jogada(3, "c")
# matriz[5][1] = "x"
imprimeMatriz(matriz)
print()