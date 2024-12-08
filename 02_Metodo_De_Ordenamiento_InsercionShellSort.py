def shell_sort(arr):
    """
    Implementa el algoritmo de ordenamiento ShellSort.

    Parámetros:
    arr (list): Lista de números a ordenar.

    Retorna:
    list: Lista ordenada.
    """
    n = len(arr)
    # Inicia con un "gap" inicial igual a la mitad del tamaño del arreglo
    gap = n // 2

    # Continúa mientras el gap sea mayor que 0
    while gap > 0:
        # Recorrer los elementos desde el índice 'gap' hasta el final
        for i in range(gap, n):
            # Guardar el valor actual que estamos evaluando
            temp = arr[i]
            j = i

            # Realizar inserción directa para elementos separados por 'gap'
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]  # Mover el elemento hacia adelante
                j -= gap  # Avanzar hacia atrás en pasos de 'gap'

            # Insertar el elemento en su posición correcta
            arr[j] = temp

        # Imprimir el estado de la lista en cada iteración del gap
        print(f"Después de usar gap {gap}: {arr}")

        # Reducir el gap para la próxima iteración
        gap //= 2

    return arr


# Ejemplo de uso
if __name__ == "__main__":
    # Lista desordenada
    lista = [23, 12, 1, 8, 34, 54, 2, 3]

    print("Lista original:", lista)

    # Ordenar la lista con ShellSort
    lista_ordenada = shell_sort(lista)

    # Imprimir la lista ordenada
    print("Lista ordenada:", lista_ordenada)
