def determinante_2x2(matriz):
    if len(matriz) != 2 or len(matriz[0]) != 2:
        raise ValueError("A matriz não é 2x2.")
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

def determinante_3x3(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("A matriz não é 3x3.")
    return (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) -
            matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) +
            matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))