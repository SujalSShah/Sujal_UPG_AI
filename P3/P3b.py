from queue import PriorityQueue

# Graph represented as:
# Node : [(Neighbour, Cost), ...]

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4)],
    'C': [('E', 2)],
    'D': [('G', 2)],
    'E': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 2,
    'E': 1,
    'G': 0
}

def a_star(start, goal):
    # Priority Queue stores (f(n), node)
    open_list = PriorityQueue()
    open_list.put((heuristic[start], start))

    # Cost from start to each node
    g_cost = {start: 0}

    # To reconstruct the path
    parent = {start: None}

    visited = set()

    while not open_list.empty():

        f, current = open_list.get()

        if current in visited:
            continue

        print("Visited:", current)
        visited.add(current)

        if current == goal:
            break

        # Explore neighbours
        for neighbour, cost in graph[current]:

            new_g = g_cost[current] + cost

            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g

                f_value = new_g + heuristic[neighbour]

                open_list.put((f_value, neighbour))

                parent[neighbour] = current

    # Reconstruct path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nShortest Path:", " -> ".join(path))
    print("Total Cost:", g_cost[goal])


# Driver Code
start = 'A'
goal = 'G'

a_star(start, goal)
