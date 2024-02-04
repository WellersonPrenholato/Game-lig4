def constroiMatriz(matriz, nc: int, nl: int):
    matriz = [['_' for _ in range(nc)] for _ in range(nl)]
    return matriz

def imprimeMatriz(matriz, nc: int, nl: int):
    indx_linha = nl
    
    for i in range(nl):
        print(f' | ' + ' | '.join(matriz[i]) + f' | {indx_linha}')
        indx_linha-=1

    # Imprimir rótulos das colunas
    rotulos_colunas = [str(i) for i in range(1, nc + 1, 1)]
    print(' | ' + ' | '.join(rotulos_colunas) + ' | ')