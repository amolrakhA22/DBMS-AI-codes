import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]  # Adjacency matrix

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # Undirected graph

    def prim_mst(self):
        # Initialize all keys as infinite and parent as -1
        key = [sys.maxsize] * self.V
        parent = [-1] * self.V
        in_mst = [False] * self.V  # Track vertices included in MST

        # Start from the first vertex
        key[0] = 0  # Make the first vertex the root of the MST
        parent[0] = -1

        for _ in range(self.V):
            # Find the vertex with the minimum key value
            min_key = sys.maxsize
            min_index = 0
            
            for v in range(self.V):
                if key[v] < min_key and not in_mst[v]:
                    min_key = key[v]
                    min_index = v
            
            # Add the chosen vertex to the MST
            in_mst[min_index] = True
            
            # Update the key and parent for the neighboring vertices
            for v in range(self.V):
                if (self.graph[min_index][v] > 0 and not in_mst[v] and
                        self.graph[min_index][v] < key[v]):
                    key[v] = self.graph[min_index][v]
                    parent[v] = min_index

        # Print the edges of the MST
        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")

# Example usage
if __name__ == "__main__":
    # Create a graph
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    # Run Prim's algorithm
    g.prim_mst()
