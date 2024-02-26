# Programa 2 Semana 11

# Ordenación en arreglo multidimensional

def ordenar_fila_ascendente(matriz, fila):

    # "Copiamos la fila para no alterar la matriz original"
    fila_ordenada = matriz[fila].copy()
    n = len(fila_ordenada)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if fila_ordenada[j] > fila_ordenada[j + 1]:
                fila_ordenada[j], fila_ordenada[j +1] = fila_ordenada[j + 1], fila_ordenada [j]
    return fila_ordenada

# Definimos la matriz

matriz = [
    [134, 15, 12],[46, 118, 12],[24, 59, 12]
]

# Imprimimos la matriz original
print("matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (índice de base 0)
fila_a_ordenar = 1

# Ordenamos la fila en orden ascendente
fila_a_ordenar:ordenar_fila_ascendente(matriz, fila_a_ordenar)

# Se actualiza la matriz con la fila ordenada
matriz[fila_a_ordenar] = fila_a_ordenar

# Se imprime la matriz con la fila ordenda
print("\nMatriz con la fila ordenada en orden ascendente:")
for fila in matriz:
    print(fila)

# Fin del programa