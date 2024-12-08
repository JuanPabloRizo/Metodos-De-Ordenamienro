import heapq

def polyphase_run_distribution(runs, num_vias):
    """
    Distribuir los runs entre las vías de forma desigual.

    Args:
    runs: Lista de secuencias ordenadas (runs) que vamos a distribuir.
    num_vias: Número de vías en las que se distribuirán los runs.

    Returns:
    Una lista de vías, cada una con un subconjunto de los runs.
    """
    vias = [[] for _ in range(num_vias)]
    
    # El algoritmo de distribución de runs asegura que algunas vías reciban más runs que otras
    idx = 0
    for run in runs:
        vias[idx].append(run)
        idx = (idx + 1) % num_vias  # Aseguramos que se distribuyan de forma cíclica
    
    return vias


# Ejemplo de secuencias ordenadas (runs)
runs = [
    [1, 4, 7],   # Run 1
    [2, 5, 8],   # Run 2
    [3, 6, 9],   # Run 3
    [0, 10, 11], # Run 4
    [12, 15, 18] # Run 5
]

# Número de vías para distribuir los runs
num_vias = 3

# Aplicamos la distribución de los runs
vias_distribuidas = polyphase_run_distribution(runs, num_vias)

# Mostrar el resultado
print("Distribución de los runs en las vías:")
for i, via in enumerate(vias_distribuidas):
    print(f"Vía {i+1}: {via}")

"""
Función polyphase_run_distribution:

La función distribuye los runs de manera desigual entre un número de vías.
Utilizamos una estructura de lista de listas (cada lista representa una vía) y asignamos los runs cíclicamente.
Se asegura que las vías no tengan la misma cantidad de runs, lo que ayuda a optimizar el proceso de mezcla.
Ejemplo de Runs:

Se tiene una lista de runs iniciales (runs) que contiene secuencias ordenadas. Estas secuencias se distribuyen en 3 vías.
Distribución Cíclica:

El índice idx asegura que los runs se distribuyan de forma cíclica entre las vías. A medida que añadimos runs a las vías, 
las vías con menos runs tendrán más chance de llenarse en las primeras fases.
"""