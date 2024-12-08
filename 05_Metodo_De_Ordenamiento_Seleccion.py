def selection_sort(arr):
    """
    Implementa el algoritmo de ordenamiento por selección (SelectionSort).

    Parámetros:
    arr (list): Lista de números a ordenar.

    Retorna:
    list: Lista ordenada.
    """
    n = len(arr)  # Obtener el tamaño de la lista

    # Recorrer todos los elementos de la lista
    for i in range(n - 1):  # n-1 porque el último elemento ya estará ordenado
        # Suponemos que el elemento actual es el mínimo
        min_index = i

        # Encontrar el índice del elemento más pequeño en la parte no ordenada
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Actualizamos el índice del elemento más pequeño

        # Si el índice mínimo ha cambiado, realizamos un intercambio
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Intercambio de valores

        # Imprimir el estado de la lista en cada iteración
        print(f"Iteración {i + 1}: {arr}")

    return arr


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo para ordenar
    lista = [64, 34, 25, 12, 22, 11, 90]

    print("Lista original:")
    print(lista)

    # Ordenar la lista usando SelectionSort
    lista_ordenada = selection_sort(lista)

    print("\nLista ordenada:")
    print(lista_ordenada)
"""
Inicialización:

n = len(arr): Calculamos el tamaño de la lista.
min_index = i: Asumimos que el elemento actual es el mínimo.
Búsqueda del mínimo:

Iteramos desde i + 1 hasta el final para encontrar el índice del valor más pequeño en la parte no ordenada.
Intercambio:

Si encontramos un valor más pequeño, lo intercambiamos con el valor en la posición actual i.
Iteraciones:

Imprimimos el estado de la lista en cada iteración para visualizar cómo se ordena.
Retorno:

Al finalizar, la lista está completamente ordenada.
"""