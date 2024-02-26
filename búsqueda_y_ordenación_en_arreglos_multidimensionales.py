# Programa 1 semana 11

# Búsqueda de arreglo multidimensional

# creamos la matriz 3x3 con números enteros
arr_matriz3x3 = [
    [12, 15, 18] , [11, 18, 2] , [4, 19, 99]
]
# Imprimimos la matriz
for (x) in arr_matriz3x3:
    print(x)
# Busqueda de un valor en la matriz
valor_buscado = 15
if any(valor_buscado in fila for fila in arr_matriz3x3):
    print(f"Se encontró {valor_buscado} en la matriz")
else:
    print(f"{valor_buscado} no se encontró en la matriz")

for fila in range(len(arr_matriz3x3)):
    for columna in range(len(arr_matriz3x3[fila])):
        if arr_matriz3x3[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda una vez encontrado el valor
    if fila_encontrada != -1:
        break  # Salir del bucle exterior si se encuentra el valor

# Verificar si se encontro el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada} ")
else:
    print(f"{valor_buscado} no se encontró en la matriz ")

# Fin del programa