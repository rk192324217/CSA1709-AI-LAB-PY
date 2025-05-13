import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = depth + self.manhattan_distance()
        
    def __lt__(self, other):
        return self.cost < other.cost
    
    def manhattan_distance(self):
        distance = 0
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x, y = divmod(self.state[i][j]-1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance
    
    def get_blank_pos(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)
    
    def get_children(self):
        children = []
        x, y = self.get_blank_pos()
        moves = [('UP', x-1, y), ('DOWN', x+1, y), 
                ('LEFT', x, y-1), ('RIGHT', x, y+1)]
        
        for move, i, j in moves:
            if 0 <= i < 3 and 0 <= j < 3:
                new_state = [row[:] for row in self.state]
                new_state[x][y], new_state[i][j] = new_state[i][j], new_state[x][y]
                children.append(PuzzleNode(new_state, self, move, self.depth+1))
        return children
    
    def get_path(self):
        path = []
        node = self
        while node:
            if node.move:
                path.append(node.move)
            node = node.parent
        return path[::-1]

def solve_8_puzzle(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    if initial_state == goal_state:
        return []
    
    open_list = []
    heapq.heappush(open_list, PuzzleNode(initial_state))
    closed_set = set()
    
    while open_list:
        current_node = heapq.heappop(open_list)
        current_state_tuple = tuple(tuple(row) for row in current_node.state)
        
        if current_state_tuple in closed_set:
            continue
            
        if current_node.state == goal_state:
            return current_node.get_path()
        
        closed_set.add(current_state_tuple)
        
        for child in current_node.get_children():
            child_state_tuple = tuple(tuple(row) for row in child.state)
            if child_state_tuple not in closed_set:
                heapq.heappush(open_list, child)
    
    return None  # No solution found

# Example usage
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = solve_8_puzzle(initial_state)
if solution:
    print("Solution found in", len(solution), "moves:")
    print(solution)
else:
    print("No solution exists")