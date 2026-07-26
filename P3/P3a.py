# P3 Greedy Best First Search .... informed Search

from queue import PriorityQueue

def greedy_best_first_search(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    visited = set()

    while not pq.empty():
        h, current = pq.get()

        if current == goal:
            print("Goal found:", current)
            return

        if current not in visited:
            visited.add(current)
            print("Visited:", current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    pq.put((heuristic[neighbor], neighbor))

    print("Goal not found")


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

greedy_best_first_search(graph, heuristic, 'A', 'G')
