def binary_search(arr, val, start, end):
    """
    Realiza una búsqueda binaria para encontrar la posición donde insertar un valor.

    Parámetros:
    arr (list): Lista ordenada en la que buscar.
    val (int): Valor que se desea insertar.
    start (int): Índice inicial del rango.
    end (int): Índice final del rango.

    Retorna:
    int: Índice donde insertar el valor.
    """
    if start == end:
        # Si el rango es único, determinar si insertar antes o después
        if arr[start] > val:
            return start
        else:
            return start + 1

    # Encontrar el punto medio
    mid = (start + end) // 2

    # Si el valor es igual al del medio, regresar esa posición
    if arr[mid] == val:
        return mid
    # Si el valor es menor que el del medio, buscar en la mitad izquierda
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid)
    # Si el valor es mayor, buscar en la mitad derecha
    else:
        return binary_search(arr, val, mid + 1, end)


def insertion_sort_binary(arr):
    """
    Ordena una lista utilizando el método de Inserción Binaria.

    Parámetros:
    arr (list): Lista de números a ordenar.

    Retorna:
    list: Lista ordenada.
    """
    # Recorrer la lista desde el segundo elemento (el primero ya está "ordenado")
    for i in range(1, len(arr)):
        # Guardar el valor actual que se desea insertar
        current_value = arr[i]
        
        # Usar búsqueda binaria para encontrar la posición correcta
        pos = binary_search(arr, current_value, 0, i)

        # Mover los elementos hacia la derecha para insertar el valor
        arr = arr[:pos] + [current_value] + arr[pos:i] + arr[i + 1:]

        # Imprimir el estado de la lista después de cada iteración
        print(f"Iteración {i}: {arr}")
    
    return arr


# Ejemplo de uso
if __name__ == "__main__":
    # Lista desordenada
    lista = [34, 23, 1, 67, 4, 90, 54]

    print("Lista original:", lista)

    # Ordenar la lista con Inserción Binaria
    lista_ordenada = insertion_sort_binary(lista)

    # Imprimir la lista ordenada
    print("Lista ordenada:", lista_ordenada)

"""
Función binary_search:

Encuentra la posición correcta donde insertar el valor actual utilizando búsqueda binaria.
Reduce el rango de búsqueda dividiendo la lista en mitades iterativamente.
Ciclo principal:

Recorre cada elemento de la lista, comenzando desde el segundo.
Busca la posición correcta para el elemento en la parte ya ordenada de la lista.
Inserción:

Ajusta los elementos para insertar el valor en su posición correcta.
Impresión:

Se imprime el estado de la lista después de cada iteración para seguir el progreso del algoritmo.
"""