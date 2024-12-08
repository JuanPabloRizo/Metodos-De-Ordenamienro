# Función para realizar el Ordenamiento por Inserción
def insertion_sort(arr):
    """
    Ordena una lista de números utilizando el algoritmo de Ordenamiento por Inserción.

    Parámetros:
    arr (list): La lista de números a ordenar.

    Retorna:
    list: La lista ordenada.
    """
    # Iterar desde el segundo elemento hasta el final de la lista
    for i in range(1, len(arr)):
        # El elemento que vamos a insertar en su posición correcta
        key = arr[i]

        # Índice de la posición inmediatamente anterior
        j = i - 1

        # Mover elementos de la sublista ordenada hacia la derecha si son mayores que la clave
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Desplazar el elemento a la derecha
            j -= 1  # Mover el índice hacia la izquierda

        # Insertar la clave en su posición correcta
        arr[j + 1] = key

        # Imprimir el estado de la lista después de cada inserción
        print(f"Iteración {i}: {arr}")

    return arr


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo desordenada
    lista = [7, 3, 5, 2, 9, 1]

    print("Lista original:", lista)

    # Llamar a la función de ordenamiento
    lista_ordenada = insertion_sort(lista)

    # Imprimir el resultado final
    print("Lista ordenada:", lista_ordenada)
