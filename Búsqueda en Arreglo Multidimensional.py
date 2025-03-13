def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"El valor {valor} se encuentra en la posición ({i}, {j})."
    return f"El valor {valor} no se encuentra en la matriz."

# Definimos una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Definimos el valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar: "))

# Llamamos a la función y mostramos el resultado
resultado = buscar_valor(matriz, valor_buscado)
print(resultado)

#Ingrese el valor a buscar: 8
#El valor 8 se encuentra en la posición (2, 1).
#Ingrese el valor a buscar: 5
#El valor 5 se encuentra en la posición (1, 1).