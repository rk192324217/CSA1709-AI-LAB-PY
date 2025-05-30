from itertools import permutations

def tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)  # Remove start node as we'll fix it as first and last
    
    min_path = None
    min_distance = float('inf')
    
    # Generate all possible paths
    for perm in permutations(nodes):
        current_distance = 0
        current_path = [start] + list(perm) + [start]
        
        # Calculate total distance for this path
        for i in range(len(current_path)-1):
            current_distance += graph[current_path[i]][current_path[i+1]]
        
        # Update minimum if found
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = current_path
    
    return min_path, min_distance

# Example usage
if __name__ == "__main__":
    # Sample graph represented as adjacency matrix
    graph = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }
    
    path, distance = tsp(graph, 'A')
    print(f"Optimal TSP Path: {path}")
    print(f"Total Distance: {distance}")