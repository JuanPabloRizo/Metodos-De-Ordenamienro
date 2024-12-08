def counting_sort(arr, exp):
    """
    Realiza Counting Sort en un arreglo basado en un dígito específico (exp).
    
    Args:
    arr: Lista de enteros.
    exp: Posición del dígito actual (10^0, 10^1, etc.).

    Returns:
    Lista ordenada por el dígito actual.
    """
    n = len(arr)  # Longitud del arreglo
    output = [0] * n  # Arreglo para almacenar los resultados ordenados
    count = [0] * 10  # Arreglo para contar ocurrencias de los dígitos (0-9)

    # Contar la frecuencia de los dígitos en la posición actual
    for i in range(n):
        index = (arr[i] // exp) % 10  # Extraer el dígito actual
        count[index] += 1

    # Acumular las frecuencias para obtener posiciones finales
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el arreglo de salida ordenado basado en el dígito actual
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar el resultado al arreglo original
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    """
    Implementa el algoritmo RadixSort para ordenar una lista de enteros.
    
    Args:
    arr: Lista de enteros a ordenar.
    
    Returns:
    Lista ordenada.
    """
    # Encontrar el número máximo para determinar el número de dígitos
    max_val = max(arr)

    # Ordenar usando Counting Sort para cada dígito, comenzando desde el LSD
    exp = 1  # Potencia de 10 (10^0, 10^1, ...)
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    lista = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", lista)

    # Ordenar usando RadixSort
    radix_sort(lista)
    print("Lista ordenada:", lista)

"""
counting_sort:

Es un subalgoritmo que clasifica los elementos según un dígito específico usando Counting Sort.
Los números se ordenan de acuerdo al dígito en la posición actual (10 k).
Se acumulan las frecuencias para calcular las posiciones finales de los elementos.
radix_sort:

Encuentra el número máximo en la lista para determinar el número de dígitos necesarios.
Itera por cada posición de los dígitos ( 10 0,10 1,10 2,…) y llama a counting_sort.
Ordenamiento:

Comienza desde el dígito menos significativo y se mueve hacia el más significativo.
Al finalizar todas las iteraciones, la lista estará ordenada.
"""