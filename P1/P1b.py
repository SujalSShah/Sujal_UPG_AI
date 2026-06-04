# P1b BFS

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start, goal):

    visited = set()
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            print("Visiting:", node)

            if node == goal:
                print("Goal reached:", goal)
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return False


goal = 'C'

if not bfs(graph, 'A', goal):
    print("Goal not found")
