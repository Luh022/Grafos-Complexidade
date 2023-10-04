class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)

    def has_cycle(self):
        visited = set()
        stack = set()

        def dfs(node):
            visited.add(node)
            stack.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in stack:
                    return True

            stack.remove(node)
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex):
                    return True

        return False

# Exemplo de uso
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')

print(graph.has_cycle())  # Saída: True

# Neste exemplo, a função 'has_cycle' 
# utiliza a busca em profundidade modificada para rastrear se algum vértice 
# é visitado mais de uma vez durante a travessia, indicando a presença de um cliclo