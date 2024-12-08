def heapify(arr, n, i):
    """
    Función para garantizar la propiedad de montículo máximo en un subárbol.
    
    Args:
    arr: Lista de elementos.
    n: Tamaño del montículo.
    i: Índice del nodo actual.
    """
    largest = i  # Asumimos que el nodo actual es el mayor.
    left = 2 * i + 1  # Índice del hijo izquierdo.
    right = 2 * i + 2  # Índice del hijo derecho.

    # Verificar si el hijo izquierdo es mayor que el nodo actual.
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verificar si el hijo derecho es mayor que el nodo más grande hasta ahora.
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el nodo actual no es el mayor, intercambiar con el más grande.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambio.
        
        # Llamar recursivamente para garantizar la propiedad en el subárbol afectado.
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Implementa el algoritmo de HeapSort para ordenar una lista.
    
    Args:
    arr: Lista de elementos a ordenar.
    """
    n = len(arr)

    # Construir el montículo máximo.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos del montículo uno por uno.
    for i in range(n - 1, 0, -1):
        # Mover la raíz actual (el mayor elemento) al final.
        arr[0], arr[i] = arr[i], arr[0]
        
        # Restaurar la propiedad de montículo en el montículo reducido.
        heapify(arr, i, 0)

# Ejemplo de uso
if __name__ == "__main__":
    lista = [12, 11, 13, 5, 6, 7]
    print("Lista original:", lista)
    heap_sort(lista)
    print("Lista ordenada:", lista)

"""
Función heapify:

Garantiza que un subárbol con raíz en el índice i satisfaga la propiedad de montículo máximo.
Si uno de los hijos del nodo raíz es mayor, se intercambian y se llama recursivamente para restaurar la propiedad de montículo en el subárbol afectado.
Función heap_sort:

Construye un montículo máximo desde la lista utilizando heapify.
Extrae repetidamente el elemento más grande (raíz del montículo) y lo coloca al final de la lista.
Reduce el tamaño del montículo y aplica heapify para mantener la propiedad.
Ejemplo de uso:

Ordena la lista [12, 11, 13, 5, 6, 7] en orden ascendente.
"""