# P1a DFS

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, goal, visited=None):

    if visited is None:
        visited = set()

    print("Visiting:", node)

    if node == goal:
        print("Goal reached:", goal)
        return True

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True

    return False


goal = 'C'

if not dfs(graph, 'A', goal):
    print("Goal not found")
