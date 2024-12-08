def bubble_sort(arr):
    """
    Implementa el algoritmo de ordenamiento por intercambio (Bubble Sort).

    Parámetros:
    arr (list): Lista de números a ordenar.

    Retorna:
    list: Lista ordenada.
    """
    n = len(arr)  # Tamaño de la lista

    # Realizar múltiples pasadas por la lista
    for i in range(n):
        # Variable para verificar si hubo intercambios
        intercambiado = False

        # Comparar elementos adyacentes
        for j in range(0, n - i - 1):  # Reducir el rango en cada iteración
            if arr[j] > arr[j + 1]:  # Cambiar a '<' para orden descendente
                # Intercambiar elementos si están en el orden incorrecto
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True  # Marcar que hubo intercambio

        # Mostrar el estado de la lista después de cada pasada
        print(f"Estado después de la iteración {i + 1}: {arr}")

        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambiado:
            break

    return arr


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    lista = [64, 34, 25, 12, 22, 11, 90]

    print("Lista original:")
    print(lista)

    # Ordenar la lista usando Bubble Sort
    lista_ordenada = bubble_sort(lista)

    print("\nLista ordenada:")
    print(lista_ordenada)
