def soma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))