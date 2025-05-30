from itertools import permutations

def solve_cryptarithmetic():
    # All unique letters in the problem
    letters = 'SENDMORY'
    digits = range(10)
    
    # Ensure all letters are unique
    assert len(set(letters)) == len(letters)
    
    # Generate all permutations of digits for the letters
    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Skip if S or M is 0 (no leading zero)
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Build numbers using the current mapping
        send = (1000 * mapping['S'] + 100 * mapping['E'] + 
                10 * mapping['N'] + mapping['D'])
        more = (1000 * mapping['M'] + 100 * mapping['O'] + 
                10 * mapping['R'] + mapping['E'])
        money = (10000 * mapping['M'] + 1000 * mapping['O'] + 
                 100 * mapping['N'] + 10 * mapping['E'] + mapping['Y'])

        # Check if the equation SEND + MORE = MONEY holds
        if send + more == money:
            print("Solution Found:")
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print("Mapping:", mapping)
            return mapping

    print("No solution found.")
    return None

# Driver code
if __name__ == "__main__":
    solve_cryptarithmetic()
