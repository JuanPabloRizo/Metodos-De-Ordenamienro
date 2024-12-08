def merge_sort(arr):
    """
    Implementa el algoritmo MergeSort para ordenar una lista.
    
    Args:
    arr: Lista de elementos a ordenar.
    
    Returns:
    Lista ordenada.
    """
    # Caso base: Si la lista tiene un solo elemento o está vacía, ya está ordenada.
    if len(arr) <= 1:
        return arr

    # Paso 1: Dividir la lista en dos mitades.
    mid = len(arr) // 2  # Encontrar el índice del medio.
    left_half = arr[:mid]  # Sublista desde el inicio hasta la mitad.
    right_half = arr[mid:]  # Sublista desde la mitad hasta el final.

    # Ordenar recursivamente ambas mitades.
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Paso 2: Mezclar ambas mitades ordenadas.
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.
    
    Args:
    left: Primera lista ordenada.
    right: Segunda lista ordenada.
    
    Returns:
    Lista combinada y ordenada.
    """
    result = []  # Lista para almacenar el resultado.
    i = j = 0  # Índices para recorrer las listas izquierda y derecha.

    # Comparar elementos de ambas listas y añadir el menor a la lista resultado.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # Añadir el elemento menor de la izquierda.
            i += 1
        else:
            result.append(right[j])  # Añadir el elemento menor de la derecha.
            j += 1

    # Añadir los elementos restantes de la izquierda (si hay).
    while i < len(left):
        result.append(left[i])
        i += 1

    # Añadir los elementos restantes de la derecha (si hay).
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    lista = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", lista)
    
    # Ordenar usando MergeSort
    lista_ordenada = merge_sort(lista)
    print("Lista ordenada:", lista_ordenada)

"""
Función merge_sort:

Si la lista tiene 1 o 0 elementos, ya está ordenada (caso base).
Divide la lista en dos mitades.
Llama recursivamente a merge_sort para cada mitad.
Une las mitades ordenadas utilizando la función merge.
Función merge:

Combina dos listas ordenadas en una sola lista ordenada.
Compara los elementos de ambas listas y los agrega al resultado en orden.
Si una lista se vacía antes que la otra, los elementos restantes de la otra lista se agregan directamente.
Ejemplo de uso:

La lista [38, 27, 43, 3, 9, 82, 10] se ordena en orden ascendente.
"""