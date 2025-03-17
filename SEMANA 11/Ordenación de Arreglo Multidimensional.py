def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def ordenar_fila(matriz, fila):
    if 0 <= fila < len(matriz):
        bubble_sort(matriz[fila])
    else:
        print("Número de fila fuera de rango")


# Definir una matriz 3x3
matriz = [
    [5, 8, 2],
    [1, 4, 7],
    [9, 3, 6]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Solicitar al usuario la fila a ordenar
fila_ordenar = int(input("Ingrese el número de la fila a ordenar (0-2): "))
ordenar_fila(matriz, fila_ordenar)

# Mostrar la matriz con la fila ordenada
print("Matriz con la fila ordenada:")
for fila in matriz:
    print(fila)

#Matriz original:
#[5, 8, 2]
#[1, 4, 7]
#[9, 3, 6]
#Ingrese el número de la fila a ordenar (0-2): 5
#Número de fila fuera de rango
#Matriz con la fila ordenada:
#[5, 8, 2]
#[1, 4, 7]
#[9, 3, 6]
