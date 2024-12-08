class Nodo:
    """
    Clase que representa un nodo en el árbol binario de búsqueda.
    """
    def __init__(self, valor):
        self.valor = valor  # Valor almacenado en el nodo
        self.izquierdo = None  # Hijo izquierdo
        self.derecho = None  # Hijo derecho


class ArbolBinarioBusqueda:
    """
    Clase para implementar un Árbol Binario de Búsqueda (BST).
    """
    def __init__(self):
        self.raiz = None  # Raíz del árbol

    def insertar(self, valor):
        """
        Inserta un nuevo valor en el árbol.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)  # Crear el nodo raíz si el árbol está vacío
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        """
        Función recursiva para insertar un valor en el árbol.
        """
        if valor < nodo.valor:  # Si el valor es menor, ir al subárbol izquierdo
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:  # Si el valor es mayor o igual, ir al subárbol derecho
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def recorrido_in_order(self):
        """
        Realiza un recorrido in-order y devuelve los valores en orden ascendente.
        """
        resultado = []
        self._in_order_recursivo(self.raiz, resultado)
        return resultado

    def _in_order_recursivo(self, nodo, resultado):
        """
        Función recursiva para realizar el recorrido in-order.
        """
        if nodo is not None:
            self._in_order_recursivo(nodo.izquierdo, resultado)  # Visitar subárbol izquierdo
            resultado.append(nodo.valor)  # Visitar nodo actual
            self._in_order_recursivo(nodo.derecho, resultado)  # Visitar subárbol derecho


def tree_sort(lista):
    """
    Implementa el algoritmo de Tree Sort.
    """
    arbol = ArbolBinarioBusqueda()
    for valor in lista:  # Insertar todos los elementos en el árbol
        arbol.insertar(valor)
    return arbol.recorrido_in_order()  # Realizar recorrido in-order


# Ejemplo de uso
if __name__ == "__main__":
    lista = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    print("Lista original:", lista)
    lista_ordenada = tree_sort(lista)
    print("Lista ordenada:", lista_ordenada)

"""
Clase Nodo:

Representa cada elemento en el árbol. Contiene un valor, un puntero al hijo izquierdo, y otro al hijo derecho.
Clase Árbol Binario de Búsqueda:

Contiene funciones para insertar valores y realizar el recorrido in-order.
La inserción garantiza que los elementos menores al nodo actual se coloquen a la izquierda, y los mayores o iguales, a la derecha.
Función tree_sort:

Crea un árbol binario de búsqueda.
Inserta todos los elementos de la lista en el árbol.
Obtiene los elementos ordenados mediante el recorrido in-order.
Ejemplo de uso:

La lista [8, 3, 10, 1, 6, 14, 4, 7, 13] se ordena como [1, 3, 4, 6, 7, 8, 10, 13, 14].
"""