import math
import queue

# ---------- GRAPH ----------
graph = {
    'A': [('B', 8), ('D', 3), ('F', 6)],
    'B': [('A', 8), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('E', 5)],
    'D': [('A', 3), ('B', 2), ('C', 1), ('E', 8), ('G', 7)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 3)],
    'F': [('A', 6), ('G', 1), ('H', 7)],
    'G': [('D', 7), ('F', 1), ('I', 1)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 1), ('H', 2), ('J', 3)],
    'J': [('E', 3), ('I', 3)]
}

# ---------- COORDINATES ----------
coordinates = {
    'A': (0, 0), 'B': (2, 1), 'C': (4, 1), 'D': (1, -2), 'E': (6, 0),
    'F': (-1, -3), 'G': (2, -4), 'H': (0, -6), 'I': (4, -5), 'J': (7, -3)
}


# ---------- FUNCTION: Generate Heuristic (Euclidean Distance) ----------
def get_heuristics(coords, goal):
    h = {}
    gx, gy = coords[goal]
    for node, (x, y) in coords.items():
        h[node] = round(math.sqrt((x - gx) ** 2 + (y - gy) ** 2), 2)
    return h


# ---------- FUNCTION: Greedy Best First Search ----------
def gbfs(graph, coords, start, goal):
    heuristics = get_heuristics(coords, goal)
    pq = queue.PriorityQueue()
    pq.put((heuristics[start], start, [start], 0))  # (priority=h, node, path, cost)
    visited = set()

    while not pq.empty():
        h, current, path, g = pq.get()

        # Goal reached
        if current == goal:
            return path, g

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                pq.put((heuristics[neighbor], neighbor, path + [neighbor], g + cost))

    return None, float('inf')


# ---------- RUN ----------
start_node = 'A'
goal_node = 'J'

path, cost = gbfs(graph, coordinates, start_node, goal_node)
print(f"Path found (GBFS): {path}")
print(f"Total cost (actual distance traveled): {cost}")
