class HashTable:
    """
    Clase que implementa una tabla hash con manejo de colisiones
    utilizando encadenamiento (listas enlazadas).
    """
    def __init__(self, size):
        """
        Inicializa una tabla hash de un tamaño dado.
        
        Parámetros:
        size (int): Tamaño de la tabla hash.
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # Crear una tabla vacía

    def hash_function(self, key):
        """
        Calcula el índice hash para una clave.
        
        Parámetros:
        key (int): Clave que se desea almacenar.
        
        Retorna:
        int: Índice hash para la clave.
        """
        return key % self.size

    def insert(self, key, value):
        """
        Inserta un par clave-valor en la tabla hash.
        
        Parámetros:
        key (int): Clave del elemento.
        value (cualquier tipo): Valor asociado a la clave.
        """
        index = self.hash_function(key)
        # Insertar el par clave-valor en la lista correspondiente
        self.table[index].append((key, value))

    def search(self, key):
        """
        Busca un valor asociado a una clave en la tabla hash.
        
        Parámetros:
        key (int): Clave que se desea buscar.
        
        Retorna:
        cualquier tipo: Valor asociado a la clave, o None si no se encuentra.
        """
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Retornar el valor si la clave coincide
        return None  # Retornar None si la clave no se encuentra

    def display(self):
        """
        Muestra el contenido de la tabla hash.
        """
        for i, bucket in enumerate(self.table):
            print(f"Índice {i}: {bucket}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una tabla hash de tamaño 5
    hash_table = HashTable(5)

    # Insertar elementos en la tabla hash
    hash_table.insert(10, "Manzana")
    hash_table.insert(15, "Plátano")
    hash_table.insert(20, "Naranja")
    hash_table.insert(25, "Uva")
    hash_table.insert(7, "Pera")

    # Mostrar la tabla hash
    print("Tabla Hash:")
    hash_table.display()

    # Buscar elementos
    print("\nBúsquedas:")
    print("Clave 10:", hash_table.search(10))  # Manzana
    print("Clave 7:", hash_table.search(7))    # Pera
    print("Clave 22:", hash_table.search(22))  # None

"""
Clase HashTable:

Implementa una tabla hash con una lista de listas (encadenamiento).
Función hash_function:

Genera un índice hash usando la operación módulo (key % size).
Método insert:

Inserta un par clave-valor en la lista correspondiente al índice hash.
Método search:

Busca un valor asociado a una clave específica, recorriendo la lista en caso de colisiones.
Método display:

Muestra todo el contenido de la tabla hash, incluyendo colisiones.
"""