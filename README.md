# EL PROBLEMA DE LAS N REINAS

En el juego de ajedrez, una reina amenaza a cualquier pieza dispuesta en su misma fila, columna o diagonal.

Deseamos disponer n reinas en un tablero de ajedrez de n x n escaques de modo que ninguna amenace a otra. Denominaremos solución a cualquier disposición de n reinas, contenga o no piezas que se amenacen, y solución factible a aquella en la que ningún par de reinas se amenazan mutuamente.

Búsqueda con retroceso

Los algoritmos de búsqueda con retroceso proponen la exploración sistémica del conjunto de soluciones hasta encontrar una factible cualquiera. La estrategia de la búsqueda con retroceso permite abordar ciertos problemas mediante un mecanismo de "casi fuerza bruta", esto es, de exploración sistemática de (potencialmente) todas las soluciones (factibles o no) hasta dar con una que sea factible. Se diferencia de la fuerza bruta en que puede decidir no explorar grandes conjuntos de soluciones cuando determina que entre ellas no hay ninguna factible.

<img width="633" height="192" alt="Captura desde 2025-11-21 17-15-43" src="https://github.com/user-attachments/assets/cfb35cc6-e8e0-4592-94ba-614e4c8f060b" />

<img width="544" height="535" alt="Captura desde 2025-11-21 17-17-58" src="https://github.com/user-attachments/assets/8d22d5f1-dde2-4d3d-b500-dba5a2f3db55" />

![IMG_20251122_184835](https://github.com/user-attachments/assets/2f1818ca-9832-4247-af97-44b20c846ca5)



