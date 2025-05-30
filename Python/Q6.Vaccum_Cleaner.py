import random

# Initialize environment
def vacuum_cleaner():
    rooms = {
        'A': random.choice(['Clean', 'Dirty']),
        'B': random.choice(['Clean', 'Dirty'])
    }
    vacuum_location = random.choice(['A', 'B'])
    actions = []

    print(f"Initial State: {rooms}, Vacuum at: {vacuum_location}")

    while 'Dirty' in rooms.values():
        # Check current room
        if rooms[vacuum_location] == 'Dirty':
            actions.append(f"Cleaned Room {vacuum_location}")
            rooms[vacuum_location] = 'Clean'
        else:
            actions.append(f"Room {vacuum_location} already clean")

        # Move to the other room
        vacuum_location = 'B' if vacuum_location == 'A' else 'A'
        actions.append(f"Moved to Room {vacuum_location}")

    print(f"\nFinal State: {rooms}")
    print("\nAction Trace:")
    for act in actions:
        print("-", act)

# Driver code
if __name__ == "__main__":
    vacuum_cleaner()
