from collections import deque

# Define the goal state
goal_state = (0, 0, 0)

# Function to check for valid states
def is_valid(state):
    M1, C1, boat = state
    M2, C2 = 3 - M1, 3 - C1  # Opposite side

    # No one can be negative
    if M1 < 0 or C1 < 0 or M2 < 0 or C2 < 0:
        return False

    # Missionaries should not be outnumbered
    if (M1 > 0 and M1 < C1) or (M2 > 0 and M2 < C2):
        return False

    return True

# BFS to find solution
def missionaries_and_cannibals():
    start = (3, 3, 1)  # 3 Missionaries, 3 Cannibals, Boat on Left
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Boat moves

    while queue:
        (M, C, B), path = queue.popleft()
        if (M, C, B) == goal_state:
            return path

        direction = -1 if B == 1 else 1  # Boat moving direction

        for m, c in moves:
            newM = M + direction * m
            newC = C + direction * c
            newB = 1 - B
            new_state = (newM, newC, newB)

            if is_valid(new_state) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None

# Driver Code
if __name__ == "__main__":
    result = missionaries_and_cannibals()
    if result:
        print("Solution Path:")
        for step in result:
            print(step)
    else:
        print("No solution found.")
