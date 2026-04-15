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

def verificaTabuleiroCheio(matriz, nc):
    """Verifica se o tabuleiro está completamente preenchido."""
    for coluna in range(nc):
        if matriz[0][coluna] == "_":
            return False
    return True