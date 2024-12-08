import heapq

def polyphase_merge(runs):
    """
    Implementación simplificada de Polyphase Sort que mezcla múltiples secuencias ordenadas en una sola secuencia ordenada.

    Args:
    runs: Lista de listas, cada una representando una secuencia ordenada de números.

    Returns:
    Una lista ordenada final combinada de todas las secuencias.
    """
    # Crear un min-heap para la mezcla eficiente de las secuencias
    heap = []
    
    # Insertar el primer elemento de cada secuencia en el heap
    for i, run in enumerate(runs):
        if run:  # Asegurarse de que la secuencia no esté vacía
            heapq.heappush(heap, (run[0], i, 0))  # (valor, índice de la secuencia, índice del elemento)

    result = []

    # Mezclar las secuencias utilizando el heap
    while heap:
        # Extraer el elemento más pequeño del heap
        value, run_idx, elem_idx = heapq.heappop(heap)
        result.append(value)

        # Si la secuencia tiene más elementos, agregar el siguiente al heap
        if elem_idx + 1 < len(runs[run_idx]):
            next_value = runs[run_idx][elem_idx + 1]
            heapq.heappush(heap, (next_value, run_idx, elem_idx + 1))

    return result


# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de secuencias ordenadas
    runs = [
        [1, 4, 7],  # Primera secuencia ordenada
        [2, 5, 8],  # Segunda secuencia ordenada
        [3, 6, 9],  # Tercera secuencia ordenada
        [0, 10, 11] # Cuarta secuencia ordenada
    ]

    print("Secuencias originales:")
    for i, run in enumerate(runs):
        print(f"Secuencia {i}: {run}")

    # Aplicar Polyphase Merge
    sorted_list = polyphase_merge(runs)

    print("\nLista ordenada final:")
    print(sorted_list)

"""
Definición de polyphase_merge:

Esta función toma una lista de listas, donde cada lista es una secuencia ordenada (un run).
Utiliza un min-heap (una estructura de datos eficiente para obtener el mínimo rápidamente) para combinar las secuencias de forma eficiente.
Uso de heapq:

Cada secuencia se inserta inicialmente con su primer elemento en el heap.
Después, en cada paso, se extrae el elemento más pequeño del heap y se añade al resultado.
Si hay más elementos en la misma secuencia, el siguiente elemento de esa secuencia se añade al heap.
Proceso de mezcla:

El heap asegura que siempre se extrae el valor más pequeño de las secuencias en cada paso.
Esto se repite hasta que todas las secuencias se combinan en una sola lista ordenada.
"""