# Programa de Python para el algortimo Dijkstra
import sys
  
class Graph():
  
    def __init__(self, vertice):
        self.V = vertice
        self.graph = [[0 for column in range(vertice)] 
                    for row in range(vertice)]
  
    def printSolution(self, dist):
        print ("Vertice Destino \tDistancia del origen hacia el destino")
        for node in range(self.V):
            print ("\t", node, "\t\t\t", dist[node])
  
     # Una funcion para encontrar el vertice con
     # valor de distancia minima, del conjunto de vertice
     # sin incluir incluir el arbol de la ruta mas corta
     
    def minDistance(self, dist, sptSet):
  
        # Inicializar la distancia minima para el siguiente nodo
        min = sys.maxint
  
        # Buscar el vertice mas cercano
        
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
  
        return min_index
  
        # algoritmo de ruta mas corta para un grafico representado 
        # usando representacion de matriz
    def dijkstra(self, src):
  
        dist = [sys.maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
  
        for cout in range(self.V):
  
            # Se elije el vertice de distancia minima de
            # el conjunto de vertice aun no procesado.
            # u siempre es igual a src en la primera iteracion
            u = self.minDistance(dist, sptSet)
  
            # Coloca el vertice de distancia minima en el 
            # arbol del camino mas corto
            sptSet[u] = True
  
            # Actualizar el valor de dist de los vertice adyacentes
            # del vertice elegido solo si el actual
            # la distancia es mayor que la nueva distancia y
            # el vertice no esta en el arbol de la ruta mas rapida
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
  
        self.printSolution(dist)
  

g = Graph(10)
        #   A  B  C  D  E  F  G  H  I  J
g.graph = [[0, 2, 6, 3, 0, 0, 0, 0, 0, 0],  #A
           [2, 0, 0, 0, 11, 0, 4, 0, 0, 0], #B
           [6, 0, 0, 2, 5, 2, 0, 0, 0, 0],  #C
           [3, 0, 2, 0, 0, 5, 0, 0, 0, 0],  #D
           [0, 11, 5, 0, 0, 1, 1, 5, 0, 0], #E
           [0, 0, 2, 5, 1, 0, 0, 0, 3, 0],  #F
           [0, 4, 0, 0, 1, 0, 0, 3, 0, 2],  #G
           [0, 0, 0, 0, 5, 0, 3, 0, 2, 1],  #H
           [0, 0, 0, 0, 0, 0, 0, 2, 0, 2],  #I
           [0, 0, 0, 0, 0, 0, 2, 1, 2, 0],  #J
        ];


# // ejercicio 2 
#         #   A  B  C  D  E  F  G  H  I  J
# g.graph = [[0, 5, 6, 4, 2, 0, 0, 0, 0, 0],  #A
#            [5, 0, 0, 0, 2, 0, 3, 0, 0, 0],  #B
#            [6, 0, 0, 1, 0, 2, 0, 1, 0, 0],  #C
#            [4, 0, 1, 0, 0, 3, 0, 0, 0, 0],  #D
#            [2, 2, 0, 0, 0, 0, 2, 3, 0, 4],  #E
#            [0, 0, 2, 3, 0, 0, 0, 0, 1, 0],  #F
#            [0, 3, 0, 0, 2, 0, 0, 0, 0, 1],  #G
#            [0, 0, 1, 0, 3, 0, 0, 0, 3, 1],  #H
#            [0, 0, 0, 0, 0, 1, 0, 3, 0, 2],  #I
#            [0, 0, 0, 0, 4, 0, 1, 1, 2, 0],  #J
#         ];
  
# // ejercicio 3 
#         #   A  B  C  D  E  F  G  H  I  J
# g.graph = [[0, 5, 4, 1, 0, 0, 0, 0, 0, 0],  #A
#            [5, 0, 1, 0, 0, 0, 2, 0, 0, 0],  #B
#            [4, 1, 0, 2, 1, 3, 0, 0, 0, 0],  #C
#            [1, 0, 2, 0, 0, 0, 0, 0, 0, 0],  #D
#            [0, 0, 1, 0, 0, 2, 2, 0, 0, 0],  #E
#            [0, 0, 3, 1, 2, 0, 1, 4, 0, 0],  #F
#            [0, 2, 0, 0, 2, 1, 0, 2, 6, 7],  #G
#            [0, 0, 0, 0, 0, 4, 2, 0, 3, 0],  #H
#            [0, 0, 0, 0, 0, 0, 6, 3, 0, 2],  #I
#            [0, 0, 0, 0, 0, 0, 7, 0, 2, 0],  #J
#         ];

# // ejercicio 4 
#         #   A  B  C  D  E  F  G  H  I  J
# g.graph = [[0, 2, 0, 1, 0, 0, 0, 0, 0, 0],  #A
#            [2, 0, 2, 0, 1, 4, 3, 0, 0, 0],  #B
#            [0, 2, 0, 4, 0, 1, 0, 0, 0, 0],  #C
#            [1, 0, 4, 0, 0, 6, 0, 0, 0, 0],  #D
#            [0, 1, 0, 0, 0, 3, 2, 0, 0, 0],  #E
#            [0, 4, 1, 6, 3, 0, 5, 2, 0, 0],  #F
#            [0, 3, 0, 0, 2, 5, 0, 2, 0, 3],  #G
#            [0, 0, 0, 0, 0, 2, 2, 0, 1, 0],  #H
#            [0, 0, 0, 0, 0, 0, 0, 1, 0, 3],  #I
#            [0, 0, 0, 0, 0, 0, 3, 0, 3, 0],  #J
#         ];

g.dijkstra(0);

# Este código es aportado por Divyanshu Mehta
