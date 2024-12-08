import heapq

def balanced_multiway_merge(runs):
    """
    Implementación de Balanced Multiway Merging.
    Mezcla múltiples secuencias ordenadas (*runs*) en una sola lista ordenada.

    Args:
    runs: Lista de listas, donde cada sublista es una secuencia ordenada.

    Returns:
    Una lista completamente ordenada.
    """
    # Crear un min-heap para realizar la mezcla
    heap = []
    
    # Insertar el primer elemento de cada run en el heap
    for i, run in enumerate(runs):
        if run:  # Asegurarse de que la run no esté vacía
            heapq.heappush(heap, (run[0], i, 0))  # (valor, índice de la run, índice del elemento)

    # Lista para almacenar el resultado final ordenado
    result = []

    # Mezclar las runs utilizando el heap
    while heap:
        # Extraer el elemento más pequeño del heap
        value, run_idx, elem_idx = heapq.heappop(heap)
        result.append(value)

        # Si hay más elementos en la misma run, añadir el siguiente al heap
        if elem_idx + 1 < len(runs[run_idx]):
            next_value = runs[run_idx][elem_idx + 1]
            heapq.heappush(heap, (next_value, run_idx, elem_idx + 1))

    return result


# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de *runs* ordenadas
    runs = [
        [1, 4, 7],  # Primera run ordenada
        [2, 5, 8],  # Segunda run ordenada
        [3, 6, 9],  # Tercera run ordenada
        [0, 10, 11] # Cuarta run ordenada
    ]

    print("Runs originales:")
    for i, run in enumerate(runs):
        print(f"Run {i}: {run}")

    # Aplicar Balanced Multiway Merging
    sorted_list = balanced_multiway_merge(runs)

    print("\nLista ordenada final:")
    print(sorted_list)
"""
Entrada de runs:

Se toma una lista de listas, donde cada sublista (run) ya está ordenada.
Uso de heapq:

Se utiliza un min-heap para manejar eficientemente la selección del menor elemento entre todas las runs.
Cada elemento en el heap es una tupla con el formato (valor, índice de la run, índice del elemento).
Proceso de mezcla:

Se extrae el elemento más pequeño del heap y se añade al resultado.
Si la run de la que proviene este elemento tiene más elementos, el siguiente elemento de esa run se añade al heap.
Resultado:

Al final, el resultado es una lista completamente ordenada.
"""