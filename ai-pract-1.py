from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Dictionary containing adjacency List

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since the graph is undirected

    # Depth First Search (Recursive)
    def dfs_recursive(self, vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    # Breadth First Search (Iterative)
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Depth First Search starting from vertex 0:")
g.dfs_recursive(0)
print("\n")

print("Breadth First Search starting from vertex 0:")
g.bfs(0)
