def rotacionar_90_graus(matriz):
    return [list(reversed(coluna)) for coluna in zip(*matriz)]