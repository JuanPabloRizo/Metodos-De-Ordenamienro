def find_runs(arr):
    """
    Identifica las runs naturales (segmentos ordenados) en la lista.
    
    Args:
    arr: Lista de elementos.
    
    Returns:
    Una lista de sublistas, donde cada sublista es una run natural.
    """
    runs = []  # Lista para almacenar las runs
    start = 0  # Índice inicial de la run actual

    for i in range(1, len(arr)):
        # Si la secuencia deja de estar ordenada
        if arr[i] < arr[i - 1]:
            runs.append(arr[start:i])  # Añadir la run actual a la lista de runs
            start = i                 # Actualizar el inicio de la siguiente run

    # Añadir la última run (si existe)
    runs.append(arr[start:])
    return runs


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


def natural_merge_sort(arr):
    """
    Implementa el algoritmo Natural Merge Sort para ordenar una lista.
    
    Args:
    arr: Lista de enteros o flotantes a ordenar.
    
    Returns:
    Lista ordenada.
    """
    # Continuar mientras haya más de una run natural
    while True:
        # Identificar las runs naturales
        runs = find_runs(arr)
        
        # Si solo queda una run, la lista ya está ordenada
        if len(runs) == 1:
            return runs[0]
        
        # Mezclar pares de runs consecutivas
        merged = []
        for i in range(0, len(runs) - 1, 2):
            merged.append(merge(runs[i], runs[i + 1]))
        
        # Si hay una run sobrante (impar), añadirla directamente
        if len(runs) % 2 == 1:
            merged.append(runs[-1])
        
        # Actualizar la lista original con las runs mezcladas
        arr = []
        for m in merged:
            arr.extend(m)


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    lista = [5, 1, 4, 2, 8, 3, 7, 6]
    print("Lista original:", lista)

    # Ordenar usando Natural Merge Sort
    lista_ordenada = natural_merge_sort(lista)
    print("Lista ordenada:", lista_ordenada)
"""
Función find_runs(arr):

Identifica las runs naturales en la lista de entrada.
Una run es una secuencia consecutiva de elementos que ya están ordenados.
Se recorre la lista y se detectan los puntos donde la secuencia deja de ser ascendente.
Función merge(left, right):

Mezcla dos listas ordenadas (left y right) en una sola lista ordenada.
Utiliza un proceso de comparación para combinar los elementos en orden.
Función natural_merge_sort(arr):

Detecta las runs naturales en la lista usando find_runs.
Mezcla iterativamente pares de runs hasta que solo quede una única run.
Si queda una run sobrante (por ejemplo, si hay un número impar de runs), esta se añade directamente al final.
Iteración:

A diferencia del merge sort tradicional, este algoritmo utiliza bucles iterativos para mezclar las runs.
En cada iteración, las runs detectadas se mezclan hasta que la lista completa esté ordenada.
"""