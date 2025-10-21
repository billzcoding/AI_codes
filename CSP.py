# --- Step 1: Define regions and their neighbors ---
regions = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'Q', 'SA'],
    'Q':  ['NT', 'NSW', 'SA'],
    'NSW': ['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'T':  ['SA']
}

# --- Step 2: Define colors ---
colors = ['red', 'green', 'blue']

# --- Step 3: Dictionary to store color assignments ---
assignment = {}

# --- Step 4: Function to check if color assignment is valid ---
def is_valid(region, color):
    for neighbor in regions[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

# --- Step 5: Backtracking function ---
def backtrack():
    # Base case: all regions colored
    if len(assignment) == len(regions):
        return True

    # Pick an uncolored region
    for region in regions:
        if region not in assignment:
            break

    # Try each color
    for color in colors:
        if is_valid(region, color):
            assignment[region] = color  # Assign color
            if backtrack():  # Recursive call
                return True
            del assignment[region]  # Backtrack

    return False  # No valid color found

# --- Step 6: Solve the problem ---
if backtrack():
    print("✅ Solution found:")
    for region, color in assignment.items():
        print(f"{region}: {color}")
else:
    print("❌ No solution found.")
