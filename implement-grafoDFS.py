class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def dfs(self, start_vertex, visited):
        visited.add(start_vertex)
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def is_connected(self):
        start_vertex = list(self.graph.keys())[0]  # Escolhe um vértice arbitrário como ponto de partida
        visited = set()
        self.dfs(start_vertex, visited)

        # Verifica se todos os vértices foram visitados
        return len(visited) == len(self.graph)

# Exemplo de uso
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')

print(graph.is_connected())  # Saída: True

# Neste exemplo, a função 'is_connect' usa a busca de profundidade (DFS) para visitar todos os vértices do grafo a partir de um vértice inicial, e então verifica se todos ps vértices foram visitados. Se todos os vértices foram visitados, o grafo é considerado conectado