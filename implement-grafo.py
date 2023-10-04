class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

    def __str__(self):
        return str(self.graph)

# Exemplo de uso
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')

print(graph.get_neighbors('A'))  # Saída: ['B']
print(graph.get_neighbors('B'))  # Saída: ['A', 'C']
print(graph)  # Saída: {'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}


# esta é uma implementação básica de um grafo não direcionado
# onde cada vértice é representado por um nó e as arestas são 
# representadas pelas conexões entre nós.

# A função 'add_vertex' adiciona um vértice ap grafo
# 'add_edge adiciona uma aresta entre dois vértices
# 'get_neighbors' retorna os vizinhos de uma vértice
# A função '__str__' é usada para imprimir o grafo