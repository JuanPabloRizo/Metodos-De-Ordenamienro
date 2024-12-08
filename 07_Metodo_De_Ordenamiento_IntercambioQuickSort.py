def quicksort(arr):
    """
    Implementa el algoritmo QuickSort para ordenar una lista.

    Parámetros:
    arr (list): Lista de elementos a ordenar.

    Retorna:
    list: Lista ordenada.
    """
    # Caso base: Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Elegir el último elemento como pivote (puede ser cualquier otro)
    pivote = arr[-1]

    # Crear sublistas para elementos menores y mayores al pivote
    menores = [x for x in arr[:-1] if x <= pivote]  # Elementos <= pivote
    mayores = [x for x in arr[:-1] if x > pivote]   # Elementos > pivote

    # Imprimir el estado actual de la lista y el pivote
    print(f"Pivote: {pivote}")
    print(f"Menores: {menores}")
    print(f"Mayores: {mayores}")

    # Llamar recursivamente a quicksort para las sublistas y combinar resultados
    return quicksort(menores) + [pivote] + quicksort(mayores)


# Ejemplo de uso
if __name__ == "__main__":
    # Lista desordenada de ejemplo
    lista = [34, 7, 23, 32, 5, 62]

    print("Lista original:")
    print(lista)

    # Ordenar la lista usando QuickSort
    lista_ordenada = quicksort(lista)

    print("\nLista ordenada:")
    print(lista_ordenada)

"""
Caso Base:

Si la lista tiene 0 o 1 elementos, ya está ordenada y se retorna directamente.
Pivote:

Seleccionamos el último elemento de la lista como pivote (pivote = arr[-1]).
División:

Usamos comprensión de listas para crear dos sublistas:
menores: Elementos menores o iguales al pivote.
mayores: Elementos mayores al pivote.
Recursión:

Llamamos recursivamente a la función quicksort para ordenar las sublistas menores y mayores.
Combinación:

Concatenamos las sublistas ordenadas y el pivote para formar la lista final.
Salida:

La lista ordenada se imprime y se retorna como resultado.
"""