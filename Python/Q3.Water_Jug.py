from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    # Each element: (jug1, jug2, path)
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        # Skip already visited states
        if (jug1, jug2) in visited:
            continue

        # Mark current state as visited
        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        # Check if target is met
        if jug1 == target or jug2 == target:
            print("Solution path:")
            for step in path:
                print(step)
            return True

        # Generate all possible next states
        possible_states = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            (min(jug1 + jug2, jug1_capacity), jug2 - (min(jug1 + jug2, jug1_capacity) - jug1)),  # Pour jug2 -> jug1
            (jug1 - (min(jug1 + jug2, jug2_capacity) - jug2), min(jug1 + jug2, jug2_capacity))   # Pour jug1 -> jug2
        ]

        for state in possible_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution found.")
    return False

# Driver code
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    water_jug_bfs(jug1_capacity, jug2_capacity, target)
