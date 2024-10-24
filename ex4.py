def multiplicar_matrizes(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("A multiplicação não é possível.")
    
    resultado = [[sum(a * b for a, b in zip(linha, coluna)) for coluna in zip(*matriz2)] for linha in matriz1]
    return resultado