def merge(left, right):
    """
    Combina dos sublistas ordenadas en una sola lista ordenada.
    
    Args:
    left: Sublista izquierda (ordenada).
    right: Sublista derecha (ordenada).
    
    Returns:
    Lista combinada y ordenada.
    """
    result = []  # Lista resultante
    i = j = 0    # Índices para recorrer las sublistas izquierda y derecha

    # Mezclar las sublistas comparando elementos
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Agregar los elementos restantes de la sublista izquierda (si los hay)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Agregar los elementos restantes de la sublista derecha (si los hay)
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def straight_merge_sort(arr):
    """
    Implementa el algoritmo Straight Merging para ordenar una lista.
    
    Args:
    arr: Lista de enteros o flotantes a ordenar.
    
    Returns:
    Lista ordenada.
    """
    n = len(arr)  # Longitud de la lista
    size = 1      # Tamaño inicial de las sublistas (1 elemento cada una)

    # Continuar mientras el tamaño de las sublistas sea menor que la longitud de la lista
    while size < n:
        for start in range(0, n, 2 * size):
            # Dividir la lista en dos sublistas: izquierda y derecha
            mid = min(start + size, n)
            end = min(start + 2 * size, n)

            # Sublistas a mezclar
            left = arr[start:mid]
            right = arr[mid:end]

            # Mezclar las sublistas y reemplazar en la lista original
            arr[start:end] = merge(left, right)

        # Duplicar el tamaño de las sublistas para la siguiente iteración
        size *= 2

    return arr


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    lista = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", lista)

    # Ordenar usando Straight Merging
    lista_ordenada = straight_merge_sort(lista)
    print("Lista ordenada:", lista_ordenada)

"""
merge(left, right):

Combina dos sublistas ordenadas (left y right) en una sola lista ordenada.
Compara los elementos de ambas sublistas y los añade a la lista result en orden.
Una vez que se agota una de las sublistas, copia los elementos restantes de la otra sublista.
straight_merge_sort(arr):

Comienza con sublistas de tamaño 
1
1.
Recorre la lista en bloques del doble del tamaño actual de las sublistas (
2
⋅
size
2⋅size).
Divide cada bloque en dos sublistas (izquierda y derecha), las mezcla y las coloca en la posición correspondiente de la lista original.
Duplica el tamaño de las sublistas en cada iteración hasta que toda la lista esté ordenada.
Proceso Iterativo:

En lugar de usar recursión para dividir la lista, este método utiliza un bucle para aumentar el tamaño de las sublistas en cada paso.
"""