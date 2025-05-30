import heapq

def heuristic(a, b):
    # Manhattan distance heuristic (for grid-based maps)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No path found

# Example usage
if __name__ == "__main__":
    # Sample graph represented as adjacency list with costs
    graph = {
        (0, 0): {(1, 0): 1, (0, 1): 1},
        (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
        (0, 1): {(0, 0): 1, (1, 1): 1},
        (1, 1): {(0, 1): 1, (1, 0): 1, (2, 1): 1},
        (2, 0): {(1, 0): 1, (2, 1): 1},
        (2, 1): {(2, 0): 1, (1, 1): 1}
    }
    
    start = (0, 0)
    goal = (2, 1)
    
    path = a_star(graph, start, goal)
    print("A* Path:", path)