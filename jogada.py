nl = 6
nc = 7

def registraJogada(matriz, indice_jogada: int, caracter: str, num_jogador: int):
    while True:
        col_jogada = (indice_jogada) - 1
        jogada_valida = False

        while not jogada_valida:
            if 0 <= col_jogada < nc:
                if matriz[0][col_jogada] != "_":
                    print(f"Coluna da jogada: {indice_jogada}")
                    print(f"*** Não é possível jogar na coluna {col_jogada + 1}!")
                    print()
                    nova_jogada = input(f"Jogador {num_jogador}, insira um novo valor: ")
                    if nova_jogada.strip() == "":
                        print("Nenhum valor foi inserido. Insira um número válido.")
                    elif nova_jogada.isdigit():
                        col_jogada = int(nova_jogada) - 1
                    else:
                        print("Valor inválido. Insira um número válido.")
                else:
                    jogada_valida = True
            else:
                print(f"Índice de jogada fora do alcance. Escolha um valor entre 1 e {nc}.")
                print()
                nova_jogada = input(f"Jogador {num_jogador}, insira um novo valor: ")
                if nova_jogada.strip() == "":
                    print("Nenhum valor foi inserido. Insira um número válido.")
                elif nova_jogada.isdigit():
                    col_jogada = int(nova_jogada) - 1
                else:
                    print("Valor inválido. Insira um número válido.")

        for i in range(nl - 1, -1, -1):
            if matriz[i][col_jogada] == "_":
                matriz[i][col_jogada] = caracter
                break
            
        return matriz