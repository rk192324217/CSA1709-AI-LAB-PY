def dfs(graph, node, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    visited.add(node)
    result.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    
    return result

# Example usage
if __name__ == "__main__":
    # Sample graph represented as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("DFS Traversal:", dfs(graph, 'A'))