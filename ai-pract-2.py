import heapq

# Define the graph as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('E', 1)],
    'E': [('B', 5), ('D', 1), ('G', 2)],
    'F': [('C', 3), ('G', 1)],
    'G': [('E', 2), ('F', 1)]
}

# Define heuristic values for each node (estimated distance to the goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 6,
    'G': 0  # Goal node has a heuristic value of 0
}

# A* Algorithm
def a_star(graph, start, goal, heuristic):
    # Priority queue to store the nodes to be explored
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Dictionaries to store the cost to reach each node and the path
    g_score = {start: 0}
    came_from = {}

    while open_set:
        # Get the node with the lowest f-score
        _, current = heapq.heappop(open_set)
        
        # If we reached the goal, reconstruct and return the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        # Explore neighbors
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                # Update the best path to reach the neighbor
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))

    return None  # Return None if no path is found

# Example usage:
start_node = 'A'
goal_node = 'G'
path = a_star(graph, start_node, goal_node, heuristic)

# Output the result
if path:
    print("Path found:", path)
else:
    print("No path found.")
