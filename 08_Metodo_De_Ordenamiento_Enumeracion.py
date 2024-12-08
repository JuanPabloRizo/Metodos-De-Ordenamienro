import itertools

def enumeracion_ordenamiento(lista):
    """
    Implementa el algoritmo de enumeración para ordenar una lista.
    Encuentra la permutación ordenada de la lista verificando todas las posibles permutaciones.

    Parámetros:
    lista (list): Lista de elementos a ordenar.

    Retorna:
    list: Lista ordenada.
    """
    # Generar todas las permutaciones posibles de la lista
    permutaciones = itertools.permutations(lista)

    for permutacion in permutaciones:
        # Comprobar si la permutación está ordenada
        if list(permutacion) == sorted(lista):
            return list(permutacion)  # Retornar la permutación ordenada

# Ejemplo de uso
if __name__ == "__main__":
    # Lista desordenada de ejemplo
    lista = [3, 1, 4, 2]

    print("Lista original:")
    print(lista)

    # Ordenar la lista usando enumeración
    lista_ordenada = enumeracion_ordenamiento(lista)

    print("\nLista ordenada:")
    print(lista_ordenada)

"""
Generación de Permutaciones:

Usamos itertools.permutations para generar todas las permutaciones posibles de la lista.
Por ejemplo, para [3, 1, 4, 2], las permutaciones serán:
(3, 1, 4, 2), (3, 1, 2, 4), (3, 4, 1, 2), ...
Comparación:

Comparamos cada permutación con la versión ordenada de la lista (sorted(lista)).
Cuando encontramos una permutación que coincide, la retornamos.
Retorno:

Una vez que encontramos la permutación ordenada, salimos del bucle y devolvemos la lista ordenada.
"""