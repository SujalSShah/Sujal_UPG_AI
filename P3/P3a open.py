# P3 Greedy Best First Search
# Includes Open node

from queue import PriorityQueue

def greedy_best_first_search(graph, heuristic, start, goal):
    open_list = PriorityQueue()
    open_list.put((heuristic[start], start))

    visited = set()

    while not open_list.empty():

        # Print Open List before selecting a node
        print("\nOpen List   :", list(open_list.queue))
        print("Visited List:", visited)

        h, current = open_list.get()

        if current == goal:
            print("\nGoal found:", current)
            return

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    open_list.put((heuristic[neighbor], neighbor))

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
