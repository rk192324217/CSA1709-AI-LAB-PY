def map_coloring(regions, neighbors, colors):
    assignment = {}
    
    def backtrack(assignment):
        if len(assignment) == len(regions):
            return assignment
        
        var = select_unassigned_region(assignment, regions)
        for color in colors:
            if is_consistent(var, color, assignment, neighbors):
                assignment[var] = color
                result = backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None
    
    def select_unassigned_region(assignment, regions):
        for region in regions:
            if region not in assignment:
                return region
    
    def is_consistent(region, color, assignment, neighbors):
        for neighbor in neighbors[region]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True
    
    return backtrack(assignment)

# Example usage
if __name__ == "__main__":
    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }
    colors = ['Red', 'Green', 'Blue']
    
    coloring = map_coloring(regions, neighbors, colors)
    print("Map Coloring Solution:", coloring)