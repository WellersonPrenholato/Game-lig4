nl = 6
nc = 13

matriz = [ [0 for i in range(nc)] for j in range(nl)]

for linha in range(nl):
    for coluna in range(nc):
        if (coluna % 2 == 0):
            matriz[linha][coluna] = "|"
        else:
            matriz[linha][coluna] = "_"
        
        
for linha in range(nl):
    for coluna in range(nc):
        print("%2s" % matriz[linha][coluna], end='')
    print()