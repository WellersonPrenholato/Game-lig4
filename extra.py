nl = 6
nc = 7

caracter_jogador_A = "O"
caracter_jogador_B = "X"

def escreveTitle():
    print("  ************************")
    print("  *****  GAME LIG 4  *****")
    print("  ************************")
    print(f"  O jogador 1 possui o caracter: {caracter_jogador_A}")
    print(f"  O jogador 2 possui o caracter: {caracter_jogador_B}")
    print()

def verificaColunaVarredura(matriz: str): #matriz[linha][coluna]
    list_column_completed = []
    for indice_col in range(nc):
        if (matriz[0][(indice_col)] != "_"): # Topo da matriz/coluna.
            list_column_completed.append(indice_col + 1)
    return list_column_completed