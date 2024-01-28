import math

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