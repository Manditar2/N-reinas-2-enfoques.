# N-reinas-2-enfoques.
En este repositorio, se presenta una solución al problema de las N reinas.

# Descripción del problema

El objetivo de este problema correspondea situar en un tablero de N×N, N reinas de tal manera que no se ataquen entre ellas.
Se busca reportar y analizar el tiempo de CPU, para varios valores de
N≥4, obtenidos al resolver este problema con Backtracking Cronológico para dos representaciones distintas.

Las primera versión corresponde a la representación del tablero como una matriz NxN, en la cual un "1" representa que se encuentra una reina situada en 
una casilla, mientras que un 0 que no. 

La segunda versión del problema sitúa el espacio de búsqueda en una lista de tamaño N, dónde cada nodo corresponde a una fila y el valor almacenado en él a la reina 
en su respectiva columna

Se utilizó la recursión como herramienta para tratar este problema, la implementación fue en Python y no requirió librerias externas.

